'''    
Created on Jan 11, 2011

@author: akai
'''
from django.contrib import admin
import models
from django.utils import log
from django.conf import settings
log.dictConfig(settings.LOGGING)
logger = log.getLogger('custom')
m = dir(models)
for i in m:
    try:
        admin.site.register(getattr(models, i))
    except Exception, e:
        pass
#map(admin.site.register, map(__import__,dir(ideab.ideabuilder.models)))


