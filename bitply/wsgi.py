"""
WSGI config for bitply project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Check if the PRODUCTION_ENV exists, if not set it to False
# and loads the normal settings
PRODUCTION_ENV = os.getenv("PRODUCTION_ENV", False)
if PRODUCTION_ENV:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bitply.prod_settings")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bitply.settings")

application = get_wsgi_application()
