from django.conf import settings
from django.core.urlresolvers import reverse
from django.test.client import Client
from django.test.testcases import TestCase
from django.utils import log
from ideab.ideabuilder.models import Builder, Project
from utils import create_test_user


log.dictConfig(settings.LOGGING)
logger = log.getLogger('custom')

class TestUser(TestCase):
    '''
    Always remember to check if the login is SUCCESSFUL
    When set password for a user, remember to SAVE it 
    '''
    def setUp(self):
        self.builder2 = create_test_user('user2@a.com')
        self.project = Project.objects.create(name='Project_Test',
                                              desc='',
                                              owner_id=self.builder2.id)

    def test_signup(self):
        c = Client()
        r = c.post(reverse('user_signup'), {'email':'user1@user1.com',
                                            'password':'user1@user1.com'})
        user = Builder.objects.get(username='user1@user1.com')

        #the new email should appear in the database
        self.assertTrue(user.email is not None)

        #the password should be hashed, means saved
        self.assertNotEqual(user.password, '')

        #test for duplicating a signup
        r = c.post(reverse('user_signup'), {'email':user.username,
                                            'password':user.username})
        #a duplicated signup should be rejected
        self.assertTrue(r.content.index('Email already in use') > -1)

    def test_apply_project(self):
        c = Client()
        builder = create_test_user('user1@a.com')
        l = c.login(username=builder.username, password=builder.username)

        r = c.post(reverse('project_apply'), {'project_id':self.project.id})

        #test if the builder should appear in the builder list of the project
        self.assertEqual(len(self.project.waitlist.filter(id=builder.id)), 1)

        r = c.post(reverse('project_apply'), {'project_id':self.project.id})
        #test if the builder apply to the same project again, it means unapply
        self.assertEqual(len(self.project.waitlist.filter(id=builder.id)), 0)

    def tearDown(self):
        pass

    def runTest(self):
        self.test_signup()

class TestOwner(TestCase):
    def setUp(self):
        #set up the owner. cred means all the username, password      
        self.owner = create_test_user('owner@a.com')
        self.project = Project.objects.create(name='Project_Test',
                                              desc='',
                                              owner_id=self.owner.id)

        #set up builder1 and builder 2
        self.builder1 = create_test_user('builder1@a.com')
        self.builder2 = create_test_user('builder2@a.com')

        #builder 1 and 2 will apply to the same project
        self.project.waitlist.add(self.builder1)
        self.project.waitlist.add(self.builder2)

        #login as the owner
        self.client = Client()

class TestOwnerChild(TestOwner):
    def test_endorse(self):
        self.client.login(username=self.owner.username, password=self.owner.username)
        self.client.post(reverse('project_endorse'),
                         {'project_id':self.project.id,
                          'waitlist_accept':[self.builder1.id, self.builder2.id]})
        #after endorsing, builder 1 should appear in the builder list of the project
        self.assertTrue(self.project.builders.filter(id=self.builder1.id))
        self.assertTrue(self.project.builders.filter(id=self.builder2.id))

    def test_illegal_endorsing(self):
        self.client.login(username=self.builder1.username, password=self.builder1.username)
        res = self.client.post(reverse('project_endorse'),
                               {'project_id':self.project.id,
                                'waitlist_accept':[self.builder1.id, self.builder2.id]})
        self.assertEqual(res.status_code, 404)
        
    def test_accept_reject(self):
        self.client.login(username=self.owner.username, password=self.owner.username)
        self.client.post(reverse('project_endorse'),
                         {'project_id':self.project.id,
                          'waitlist_accept':[self.builder1.id],
                          'waitlist_reject':[self.builder2.id]})
        #after endorsing, builder 1 should appear in the builder list of the project
        self.assertTrue(self.project.builders.filter(id=self.builder1.id))
        #builder2 should be gone forever!
        self.assertTrue(not self.project.waitlist.filter(id=self.builder2.id))