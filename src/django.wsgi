import os
import sys

sys.path.append('/var/python/django/place-db')
sys.path.append('/var/python/django/place-api')
os.environ['DJANGO_SETTINGS_MODULE'] = 'place.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()