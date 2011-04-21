from django.db import models
from django.contrib.auth.admin import User

class Project(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField()
    owner = models.ForeignKey(User, related_name='only_owner')
    builder = models.ManyToManyField(User, related_name='builders')      

class Builder(User):
    credit_no = models.IntegerField(default=0)   
    
class Task(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField()
    project = models.ForeignKey(Project)
    task = models.ManyToManyField(Builder)
    
class SkillCategory(models.Model):
    name = models.CharField(max_length=20)        
    pass

class Skill(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(SkillCategory)
    pass       


