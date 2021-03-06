"""
Django Production Settings for bitply project.
"""

import utils
import dj_database_url


try:
    from .settings import *
except ImportError as e:
    raise ImportError("Error: failed to import settings module ({})".format(e))

PRODUCTION_ENV = utils.get_env("PRODUCTION_ENV", False)
DEBUG = utils.get_env("DEBUG", False)
TEMPLATE_DEBUG = utils.get_env("TEMPLATE_DEBUG", False)
SECRET_KEY = os.getenv("SECRET_KEY")

# Update database configuration with $DATABASE_URL.
DB_FROM_ENV = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(DB_FROM_ENV)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Heroku configuration static-files
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
