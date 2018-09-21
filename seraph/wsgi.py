"""
WSGI config for seraph project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""
import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

# Use heroku platform if not set
platform = os.getenv('SERAPH_PLATFORM', 'heroku')

if platform == 'dev':
    settings = 'seraph.settings.dev'
elif platform == 'heroku':
    settings = 'seraph.settings.heroku'
else:
    settings = 'seraph.settings.prod'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)

application = get_wsgi_application()

# Use WhiteNoise to serve static assets on heroku
if platform == 'heroku':
    application = DjangoWhiteNoise(application)
