'''
Created on Jan 12, 2011

@author: akai
'''
from ..models import Builder
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.utils import log
from django.conf import settings
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
#            login(request, user)
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

