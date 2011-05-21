'''
Created on Apr 21, 2011

@author: akai
'''
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.forms.models import ModelForm
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext
from django.utils import log
from django.views.decorators.csrf import csrf_protect
from django.views.generic.list_detail import object_detail
from django.views.generic.simple import redirect_to
from ideab.ideabuilder.constants import PROJECT_DETAIL_TEMPLATE, \
    PROJECT_ADD_TEMPLATE
from ideab.ideabuilder.models import Project, Builder

log.dictConfig(settings.LOGGING)
logger = log.getLogger('custom')

@login_required
def project_detail(request, object_id):
    project = get_object_or_404(Project, pk=object_id)
    return object_detail(request,
                         Project.objects.all(),
                         object_id,
                         template_name=PROJECT_DETAIL_TEMPLATE,

                         extra_context={'builder_list': project.builders.all()})
    
    
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ['owner', 'builders', 'waitlist']
        
    
@csrf_protect    
@login_required
def add(request):
    if request.method == 'POST':
        form = ProjectForm(data=request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return HttpResponseRedirect(reverse('project_detail',
                                                kwargs={'object_id':project.id}))
    else: 
        form = ProjectForm()
    return render_to_response(PROJECT_ADD_TEMPLATE,
                              {'form':form,
                               'url': reverse('project_add'),
                               'title':'Adding a project'},
                              RequestContext(request)) 
    
@csrf_protect    
@login_required
def delete(request):
    if request.method == 'POST':
        try:
            project = Project.objects.get(id=request.POST['id'])
            project.delete()
        except Project.DoesNotExist, e:
            pass
    return HttpResponseRedirect(reverse('project_list'))
