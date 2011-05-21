from django.contrib.auth.admin import User
from django.contrib.auth.backends import ModelBackend
from django.core.urlresolvers import reverse
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    desc = models.TextField()
    owner = models.ForeignKey(User, related_name='only_owner')
    builders = models.ManyToManyField(User, related_name='builders')   
    waitlist = models.ManyToManyField(User)     
    
    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'object_id':self.id})
    
    def __unicode__(self):
        return self.name
    
class Builder(User):
    name = models.CharField(max_length=200, default='Unknown')
    credit_no = models.IntegerField(default=0)   
    user = models.ForeignKey(User, unique=True, null=True, related_name='linked_user')
    nationality = models.CharField(max_length=50, default='Unknown')
    university = models.CharField(max_length=200, default='Unknown')        
    
class Task(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField()
    project = models.ForeignKey(Project)
    builders = models.ManyToManyField(Builder)
    
    def __unicode__(self):
        return self.name
    
class SkillCategory(models.Model):
    name = models.CharField(max_length=20)   

    def __unicode__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(SkillCategory)
    
    def __unicode__(self):
        return "%s:%s" % (self.category, self.name)

