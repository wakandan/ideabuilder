'''
Created on Jan 12, 2011

@author: akai
'''
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django import forms 
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required


class UserForm(forms.Form):
    username = forms.CharField(max_length=10)
    email = forms.EmailField(max_length=20)
    password1 = forms.CharField(max_length=20,
                                widget=forms.PasswordInput(render_value=False))
    password2 = forms.CharField(max_length=20,
                                widget=forms.PasswordInput(render_value=False))
    
    def clean_username(self):
        try:
            User.objects.get(username=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError("Username already in use")
    def clean(self):
        if 'password1' not in self.cleaned_data or \
            'password2' not in self.cleaned_data or \
            self.cleaned_data['password1']!=self.cleaned_data['password2']:
            raise forms.ValidationError("Passwords don't match")
        return self.cleaned_data

    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], 
                                 email=self.cleaned_data['email'], 
                                 password=self.cleaned_data['password1'])
    
@csrf_protect
def add_user(request):
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user_profile'))
    else:    
        form = UserForm()
    return render_to_response('user_signup.html', {'form':form},
                              RequestContext(request))
    
@login_required
def user_profile(request):
    return render_to_response('user_profile.html')
