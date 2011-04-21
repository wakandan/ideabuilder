'''
Created on Apr 21, 2011

@author: akai
'''
from django.contrib.auth.decorators import login_required
from ideab.ideabuilder.models import Project, Builder
from django.shortcuts import get_object_or_404, render_to_response
from django.views.generic.list_detail import object_detail
from ..constants import *


@login_required
def project_detail(request, object_id):
    project = get_object_or_404(Project, pk=object_id)
    return object_detail(request,
                         Project.objects.all(),
                         object_id,
                         template_name=PROJECT_DETAIL_TEMPLATE,
                         extra_context={'builder_list': project.project_builder.all()})
    