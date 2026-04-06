import os
import sys

# 1. Loyihang joylashgan papka (Katta-kichik harfiga qara!)
path = '/home/Burik/Exolex'
if path not in sys.path:
    sys.path.append(path)

# 2. Settings fayli qayerda?
# Agar settings.py fayling 'config' degan papkada bo'lsa:
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

# 3. Djangoni ishga tushirish
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()