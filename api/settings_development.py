from .settings import *

DEBUG = True
ADMINS = []
ALLOWED_HOSTS = ['0.0.0.0']
#INSTALLED_APPS.append('debug_toolbar')
#MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE
#DEBUG_TOOLBAR_PATCH_SETTINGS = False
#
#
#def custom_show_toolbar(request):
#    return True  # Always show toolbar, for example purposes only.
#
#
#DEBUG_TOOLBAR_CONFIG = {
#    'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
#}

STATIC_ROOT = None
