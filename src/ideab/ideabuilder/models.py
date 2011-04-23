from django.contrib.auth.admin import User
from django.contrib.auth.backends import ModelBackend
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=20, unique=True)
    desc = models.TextField()
    owner = models.ForeignKey(User, related_name='only_owner')
    builders = models.ManyToManyField(User, related_name='builders')      

class Builder(User):
    credit_no = models.IntegerField(default=0)   
    user = models.ForeignKey(User, unique=True, null=True, related_name='linked_user')
    
class Task(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField()
    project = models.ForeignKey(Project)
    builders = models.ManyToManyField(Builder)
    
class SkillCategory(models.Model):
    name = models.CharField(max_length=20)        
    pass

class Skill(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(SkillCategory)
    pass       

#class BuilderAuthenticationBackend(ModelBackend):
#    def authenticate(self, username, password):
#        try: 
#            user = Builder.objects.get(username=username)
#            if user.check_password(password):
#                return user
#        except Builder.DoesNotExist, e:
#            return None

