
import time
import threading

import requests


def ping_site():
    # Saytingizning Render-dagi URL manzilini bering
    URL = "https://sizning-saytingiz.onrender.com"

    while True:
        try:
            response = requests.get(URL)
            print(f"Ping muvaffaqiyatli: {response.status_code}")
        except Exception as e:
            print(f"Pingda xatolik: {e}")

        # Har 10 daqiqada (600 soniya) ping jo'natadi
        # Render 15 daqiqa harakatsizlikdan keyin uxlab qoladi
        time.sleep(600)


def start_ping():
    # Asosiy serverga xalaqit bermasligi uchun alohida thread-da ishga tushiramiz
    thread = threading.Thread(target=ping_site, daemon=True)
    thread.start()