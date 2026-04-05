#!/usr/bin/env bash
set -o errexit

echo ">>> Kutubxonalar o'rnatilmoqda..."
pip install -r requirements.txt

echo ">>> Statik fayllar yig'ilmoqda..."
python manage.py collectstatic --noinput

echo ">>> Ma'lumotlar bazasi migratsiya qilinmoqda..."
python manage.py migrate

echo ">>> Superuser yaratish jarayoni..."
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); \
if not User.objects.filter(username='admin').exists(): \
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123'); \
    print('Superuser yaratildi!'); \
else: \
    print('Superuser allaqachon mavjud.')"

echo ">>> Build jarayoni muvaffaqiyatli yakunlandi!"