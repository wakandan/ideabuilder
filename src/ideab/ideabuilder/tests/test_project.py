'''
Created on Apr 22, 2011

@author: akai
'''
from ..models import Builder, Project, Task
from ..views import project
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test.client import Client
from django.test.testcases import TestCase
from django.utils import log
from utils import create_test_user
log.dictConfig(settings.LOGGING)
logger = log.getLogger('custom')

class TestProject(TestCase):
    def setUp(self):
        self.owner = create_test_user('owner@a.com')
        self.builder1 = create_test_user('builder1@a.com')
        self.builder2 = create_test_user('builder2@a.com')
        pass
#    def test_view_project(self):        
#        c = Client()
#        c.login(username='user1', password='user1')
#        project = Project.objects.create(name='test',
#                                          desc='test',
#                                          owner=self.user1)
#        project = Project.objects.get(name='test')
#        r = c.get('/ideabuilder/project/%d/' % project.id)                
#        print 'content: [%s]' % r.content
#        self.assertTrue(r.content.index('test')>=0)        
#        pass
    def test_add_project(self):
        c = Client()
        #test if the project can be added
        l = c.login(username=self.owner.username, password=self.owner.username)
        self.assertTrue(l)
        r = c.post(reverse('project_add'), {'name':'project1',
                                                'desc':'project1'})
        project = Project.objects.filter(name='project1')
        self.assertTrue(project)

        #test if we should not add 2 projects with the same name
        r = c.post(reverse('project_add'), {'name':'project1',
                                                'desc':'project1'})
        self.assertNotEqual(r.content.index('already exists'), -1)
        pass

    def test_del_project(self):
        c = Client()
        l = c.login(username=self.owner.username, password=self.owner.username)
        self.assertTrue(l)
        project = Project.objects.create(name='project1',
                                         desc='project1',
                                         owner=self.owner)
        r = c.post(reverse('project_del'), {'id':project.id})
        self.assertEqual(r.status_code, 302)
        with self.assertRaises(Project.DoesNotExist):
            Project.objects.get(id=project.id)

        #try to delete a non-existent project
        r = c.post(reverse('project_del'), {'id':project.id})
        self.assertEqual(r.status_code, 302)


    def tearDown(self):

        pass

