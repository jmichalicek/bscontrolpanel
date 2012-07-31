from django import template
from bsproject.models import Language

register = template.Library()

def registered_views():
    from bscontrolpanel import site
    return site._registry.copy()

register.assignment_tag(registered_views)
