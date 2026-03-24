import os
import subprocess
import sys


def run_command(command):
    print(f"Bajarilmoqda: {command}")
    process = subprocess.Popen(command, shell=True)
    process.wait()


def setup():
    # 1. Migratsiya fayllarini yaratish
    run_command("python manage.py makemigrations")

    # 2. Bazaga migratsiya qilish
    run_command("python manage.py migrate")

    # 3. Superuser yaratish (Avtomatik)
    # Eslatma: Buni faqat bir marta ishlatish kerak
    print("Superuser yaratishga urinilmoqda...")
    username = "admin"
    email = "admin@example.com"
    password = "123"

    # Superuser yaratish kodi (Interaktiv bo'lmagan usul)
    from django.contrib.auth import get_user_model
    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'loyiha_nomi.settings')  # 'loyiha_nomi'ni o'zgartiring
        import django
        django.setup()
        User = get_user_model()
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            print(f"Superuser yaratildi: {username} / {password}")
        else:
            print("Superuser allaqachon mavjud.")
    except Exception as e:
        print(f"Xato: {e}")

    # 4. Serverni ishga tushirish
    run_command("python manage.py runserver")


if __name__ == "__main__":
    setup()