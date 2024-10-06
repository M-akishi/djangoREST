"""
WSGI config for djangoREST project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application


sys.path.append('/var/www/html/djangoREST')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoREST.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
