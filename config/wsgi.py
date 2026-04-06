import os
import sys

# 1. Loyihang joylashgan papka manzili
# Rasmingda loyiha nomi 'Exolex' (kichik harf bilan)
path = '/home/Burik/Exolex'
if path not in sys.path:
    sys.path.append(path)

# 2. Django settings fayliga yo'l
# Rasmingda settings.py fayli 'config' degan papkada turibdi
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

# 3. WSGI dasturini ishga tushirish
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()