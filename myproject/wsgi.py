"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# 1. It tells the server where your settings are
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

# 2. This 'application' variable is what Gunicorn 'holds onto'
application = get_wsgi_application()
