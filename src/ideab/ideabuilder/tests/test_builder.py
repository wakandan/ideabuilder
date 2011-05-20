from ..models import Builder, Project, Task
from ..views import project
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test.client import Client
from django.test.testcases import TestCase
from django.utils import log
from ideab.ideabuilder.views.builder import user_login


log.dictConfig(settings.LOGGING)
logger = log.getLogger('custom')

class TestUser(TestCase):
    '''
    Always remember to check if the login is SUCCESSFUL
    When set password for a user, remember to SAVE it 
    '''
    def setUp(self):
        self.builder2 = Builder.objects.create(username='user2@a.com',
                                             email='user2@a.com')
        self.builder2.set_password('user2@a.com')     
        self.project = Project.objects.create(name='Project_Test',
                                              desc='',
                                              owner_id=self.builder2.id)                
        pass
    
    def test_signup(self):
        c = Client()
        r = c.post(reverse('user_signup'), {'email':'user1@user1.com',
                                            'password':'user1@user1.com'})
        user = Builder.objects.get(username='user1@user1.com')        
        
        #the new email should appear in the database
        self.assertTrue(user.email is not None)
        
        #the password should be hashed, means saved
        self.assertNotEqual(user.password, '')
    
    
    def test_signup_duplicate_user(self):
        c = Client()
        user = Builder.objects.create(username='user1@user1.com',
                                      email='user1@user1.com')
        user.set_password('user1@user1.com')
        user.save()
        r = c.post(reverse('user_signup'), {'email':'user1@user1.com',
                                            'password':'user1@user1.com'})
        #a duplicated signup should be rejected
        self.assertTrue(r.content.index('Email already in use') > -1)
        
    def test_login(self):
        c = Client()
        l = c.post(reverse('user_signup'), {'email':'user1@user1.com',
                                            'password':'user1@user1.com'})
        user = Builder.objects.get(username='user1@user1.com')
        self.assertNotEqual(user.password, '')
        l = c.login(username=user.username,
                    password='user1@user1.com')        
        self.assertEqual(l, True)        
        
    def test_apply_project(self):
        c = Client()
        builder = Builder.objects.create(username='user1@a.com',
                                         email='user1@a.com')
        builder.set_password('user1@a.com')   
        builder.save()     
        l = c.login(username=builder.username, password='user1@a.com')
        r = c.post(reverse('project_apply'), {'project_id':self.project.id})
        
        #test if the builder should appear in the builder list of the project
        self.assertEqual(len(self.project.builders.filter(id=builder.id)), 1)        
        pass
    
    def test_endorse(self):
        pass
    
    def tearDown(self):        
        pass
