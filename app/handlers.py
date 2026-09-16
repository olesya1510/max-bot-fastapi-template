"""
Обработка входящих апдейтов от MAX. В этом шаблоне — только команда /start,
остальная логика (бизнес-сценарии, база данных и т.д.) специфична для
конкретного проекта и сюда намеренно не включена.
"""

from app.config import BOT_TOKEN, API_BASE_URL
from app.max_client import MaxClient

client = MaxClient(BOT_TOKEN, API_BASE_URL)


async def handle_update(update: dict) -> None:
    update_type = update.get("update_type")

    if update_type == "message_created":
        message = update.get("message", {})
        chat_id = message.get("recipient", {}).get("chat_id")
        text = message.get("body", {}).get("text", "").strip().lower()

        if chat_id is None:
            return

        if text in ("/start", "старт"):
            await client.send_message(chat_id, "Привет! Бот работает 🤖")
