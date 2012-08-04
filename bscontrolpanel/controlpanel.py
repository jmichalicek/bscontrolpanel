from django.template.defaultfilters import slugify
from django.conf.urls import patterns, url, include
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core.urlresolvers import reverse

import logging
logger = logging.getLogger(__name__)

class PathAlreadyRegistered(Exception):
    pass

class ControlPanel(object):
    """
    Manages the control panel for the site's apps
    """

    def __init__(self):
        self._registry = {}
        self.app_name = 'bscontrolpanel'
        self.name = 'bscontrolpanel'

    def register(self, app_name, view, printable_name=None, view_path=None):
        """Register control panel views with the control panel"""

        if view_path is None:
            view_path = slugify(view.func_name)

        if printable_name is None:
            printable_name = view_path

        if app_name not in self._registry:
            self._registry[app_name] = []


        # Kind of ugly, but these shouldn't be very big
        for v in self._registry[app_name]:
            if v[1] == view_path:
                raise PathAlreadyRegistered('The path %s is already registered for app_name %s' %(view_path, app_name))

        self._registry[app_name].append((view, view_path, 'bscontrolpanel:%s' %view_path, printable_name))

    def get_urls(self):
        urlpatterns = patterns('',
                               url(r'^$', 'bscontrolpanel.views.index', name='index'),
                               url(r'login/', 'bscontrolpanel.views.login',
                                   {'template_name': 'bscontrolpanel/login.html'},
                                   name="login"),
                               url(r'logout/', 'django.contrib.auth.views.logout_then_login',
                                   name='logout_and_in'),
                               )
        for app, views in self._registry.iteritems():
            for view in views:
                urlpatterns += patterns('',
                                        url(r'^%s/%s/' %(app, view[1]),
                                            view[0], name=view[1])
                                        )

        return urlpatterns

    @property
    def urls(self):
        return self.get_urls(), self.app_name, self.name


site = ControlPanel()
