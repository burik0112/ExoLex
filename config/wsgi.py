import os
import sys

# Loyiha yo'li
path = '/home/Burik/Exolex'
if path not in sys.path:
    sys.path.append(path)

# config - bu settings.py fayli turgan papka nomi
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()