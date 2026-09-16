"""
Конфигурация шаблона. Все секреты — только через переменные окружения (.env),
никогда не хардкодятся в коде.
"""

import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "")  # публичный HTTPS-адрес, куда MAX будет слать апдейты

API_BASE_URL = "https://botapi.max.ru"
