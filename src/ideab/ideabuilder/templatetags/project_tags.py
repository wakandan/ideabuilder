'''
Created on May 21, 2011

@author: akai
'''
from django import template
from django.db.models import get_model
from ideab.ideabuilder.constants import get_logger
logger = get_logger()
def do_check_project_applied(parser, token):
    #split token to get arguments
    bits = token.split_contents()
    if len(bits)!=2:
        raise template.TemplateSyntaxError("'check_project_applied' takes 1 argument")
    
    class WaitListStatusNode(template.Node):
        def __init__(self, project):
            self.project = template.Variable(project)            
        def render(self, context):
            try:
                project = self.project.resolve(context)
                user = template.Variable('user').resolve(context)
                if len(project.builders.filter(id=user.id))==1:
                    return 'Unapply'
                else:
                    return 'Apply'
            except template.VariableDoesNotExist:
                return ''
            pass
    return WaitListStatusNode(bits[1])

register = template.Library()
register.tag('check_project_applied', do_check_project_applied)