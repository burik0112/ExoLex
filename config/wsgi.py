import os
import sys

# 1. Loyihang turgan aniq yo'l
path = '/home/Burik/Exolex'
if path not in sys.path:
    sys.path.append(path)

# 2. Settings qayerda?
# Agar settings.py fayling 'config' papkasida bo'lsa:
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
# AGAR 'config' papkasi bo'lmasa, unda 'Exolex.settings' deb yozib ko'r.

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()