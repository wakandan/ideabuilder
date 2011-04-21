from constants import *
from django.conf.urls.defaults import patterns
from models import Project
from views.builder import user_signup, user_login, user_profile
import logging

urlpatterns = patterns('',
    #(r'^signup/$', builder.user_signup, {'template_name':'user_signup.html'}, 'user_signup'),
    (r'^signup/', user_signup, {}, 'user_signup'),
    (r'^login/', 'django.contrib.auth.views.login', {'template_name':'user_login.html'}, 'user_login'),    
    (r'^logout/', 'django.contrib.auth.views.logout', {'template_name':'user_logout.html'}, 'user_logout'),
    (r'^profile/', user_profile, {}, 'user_profile'),
) 




project_dict = {'queryset': Project.objects.all()}
urlpatterns += patterns('',
    (r'project/$', 'django.views.generic.list_detail.object_list', 
        dict(project_dict, 
             template_name=PROJECT_LIST_TEMPLATE,
             paginate_by=20), 
        'project_list'),
    (r'project/(?P<object_id>\d+)/$', 'ideabuilder.views.project.project_detail',
        {},     
        'project_detail'),
)
