'''
Created on Jan 12, 2011

@author: akai
'''
from ..models import Builder
from django import forms
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.utils import log
from django.views.decorators.csrf import csrf_protect
from ideab.ideabuilder.models import Project

log.dictConfig(settings.LOGGING)
logger = log.getLogger('custom')


class UserForm(forms.Form):
    email = forms.EmailField(max_length=20)
    password = forms.CharField(max_length=20,
                               widget=forms.PasswordInput(render_value=False))

    def clean_email(self):
        try:
            Builder.objects.get(username=self.cleaned_data['email'])
        except Builder.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError("Email already in use")

    def save(self):
        new_builder = Builder.objects.create(username=self.cleaned_data['email'],
                                             email=self.cleaned_data['email'])
        new_builder.set_password(self.cleaned_data['password'])
        new_builder.save()


@csrf_protect
def user_signup(request):
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserForm()
    return render_to_response('user_signup.html', {'form':form},
                              RequestContext(request))

@login_required
def user_profile(request):
    return render_to_response('user_profile.html')

def user_login(request):
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username,
                            password=password)
        if user is not None:
            return HttpResponseRedirect(reverse('index'))
        else:
            form.errors['message'] = 'Invalid login'
    else:
        form = UserForm()
    return render_to_response('user_login.html', {'form':form},
                              RequestContext(request))

@csrf_protect
@login_required
def apply(request):
    '''
    Add the current user as a builder to viewing project's builder
    wait list. The idea owner will have to endorse this user manually
    so that the guy can officially take part in the project.
    
    Object_id is the project_id that the guy wants to apply to, it will 
        be passed in the url. The html page should confirm with the user
        before the request should be sent
    '''
    def add_project(builder, project):
        '''Take care of the logic of adding the project to a builder'''
        pass
    if request.method == 'POST':
        user = request.user
        project_id = request.POST['project_id']
        project = get_object_or_404(Project, pk=project_id)
        if not project.waitlist.filter(id=user.id):
            logger.debug("%s|apply|adding userid %d to projectid %d's waitlist" % (__name__, user.id, project.id))
            project.waitlist.add(user)
        else:
            logger.debug("%s|apply|removing userid %d from projectid %d's waitlist" % (__name__, user.id, project.id))
            project.waitlist.remove(user)
    return HttpResponseRedirect(reverse('project_list'))


@csrf_protect
@login_required
def endorse(request, accept=True):
    '''
    For an idea owner to endorse a builder in the project's wait list.
    accept=True means accepted, accept=False means rejected
    '''
    pass
