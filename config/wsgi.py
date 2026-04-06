import os
import sys

# Loyiha yo'li
path = '/home/burik0112/ExoLex'
if path not in sys.path:
    sys.path.append(path)

# Settings fayli manzili. Loyiha papkang 'config' bo'lsa:
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()