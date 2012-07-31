from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.cache import never_cache
from django.contrib.auth import REDIRECT_FIELD_NAME

@login_required()
def index(request):
    return render_to_response(
        'bscontrolpanel/index.html',
        {},
        context_instance=RequestContext(request))


@never_cache
def login(request, template_name='bscontrolpanel/login.html'):
    """
    Displays the login form for the given HttpRequest.
    """

    # This view has to exist because the reverse('bscontrolpanel:index') doesn't
    # work in the args in urls.py to just use django.contrib.auth.views.login
    # directly.
    #
    # Is this overkill?  Could just use the regular django.contrib.auth.views.login
    # and set settings.LOGIN_REDIRECT_URL.  Initial thought was that there could be
    # login for the control panel and some other sort of user login using LOGIN_REDIRECT_URL
    # but this may be overengineering for something that won't exist.
    # Leaving in for now... allows the app to work with less config to remember to do

    redirect_to = request.REQUEST.get(REDIRECT_FIELD_NAME, '')
    if redirect_to == '':
        redirect_to = reverse('bscontrolpanel:index')

    defaults = {
        'template_name': template_name,
        'extra_context': {REDIRECT_FIELD_NAME: redirect_to}
        }

    return auth.views.login(request, **defaults)
