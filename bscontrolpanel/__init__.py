from controlpanel import ControlPanel, site

def autodiscover():
    """
    Find all apps in INSTALLED_APPS which have control panel views
    and ensure that the views are registered.
    """

    import copy
    from django.conf import settings
    from django.utils.importlib import import_module

    for app in settings.INSTALLED_APPS:
        import_module(app)
        try:
            original_registry = copy.copy(site._registry)
            import_module('%s.controlpanel' % app)
        except:
            site._registry = original_registry
