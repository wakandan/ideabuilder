'''
Created on May 21, 2011

@author: akai
'''
from ideab.ideabuilder.models import Builder


def create_test_user(credential):
    '''To create a test user'''
    user = Builder.objects.create(username=credential,password=credential)
    user.set_password(credential)
    user.save()
    return user    