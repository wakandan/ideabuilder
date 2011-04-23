from ..models import Builder, Project, Task
from ..views import project
from django.test.client import Client
from django.test.testcases import TestCase
from django.contrib.auth.models import User
from django.conf import settings
from django.core.urlresolvers import reverse
from ideab.ideabuilder.views.builder import user_login
from django.utils import log
log.dictConfig(settings.LOGGING)
logger = log.getLogger('custom')

class TestUser(TestCase):
    def setUp(self):
        pass
    
    def test_signup(self):
        c = Client()
        r = c.post(reverse('user_signup'), {'email':'user1@user1.com',
                                            'password':'user1@user1.com'})
        user = Builder.objects.get(username='user1@user1.com')        
        self.assertTrue(user.email is not None)
        self.assertNotEqual(user.password, '')
    
    
    def test_signup_duplicate_user(self):
        c = Client()
        user = Builder.objects.create(username='user1@user1.com',
                                      email='user1@user1.com')
        user.set_password('user1@user1.com')
        user.save()
        r = c.post(reverse('user_signup'), {'email':'user1@user1.com',
                                            'password':'user1@user1.com'})
        self.assertTrue(r.content.index('Email already in use')>-1)
        
    def test_login(self):
        c = Client()
        l = c.post(reverse('user_signup'), {'email':'user1@user1.com',
                                            'password':'user1@user1.com'})
        user = Builder.objects.get(username='user1@user1.com')
        self.assertNotEqual(user.password, '')
        l = c.login(username=user.username, 
                    password='user1@user1.com')        
        self.assertEqual(l, True)        
        

    def tearDown(self):        
        pass