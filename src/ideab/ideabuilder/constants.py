'''
Created on Apr 21, 2011

@author: akai
'''

from django.utils import log
from django.conf import settings

def get_logger():
    log.dictConfig(settings.LOGGING)
    return log.getLogger('custom')
    
PROJECT_LIST_TEMPLATE = 'project_list.html'
PROJECT_DETAIL_TEMPLATE = 'project_detail.html'
PROJECT_ADD_TEMPLATE = 'object_add.html'
OBJECT_ADD_TEMPLATE = 'object_add.html'
