"""
Разовый скрипт регистрации вебхука бота в MAX.
Запустить один раз после деплоя (когда WEBHOOK_URL уже публично доступен):

    python register_webhook.py
"""

import asyncio

import aiohttp

from app.config import BOT_TOKEN, WEBHOOK_URL, API_BASE_URL


async def main() -> None:
    if not BOT_TOKEN or not WEBHOOK_URL:
        print("Заполните BOT_TOKEN и WEBHOOK_URL в .env перед запуском.")
        return

    headers = {"Authorization": BOT_TOKEN, "Content-Type": "application/json"}
    payload = {"url": WEBHOOK_URL, "update_types": ["message_created"]}

    async with aiohttp.ClientSession() as session:
        async with session.post(f"{API_BASE_URL}/subscriptions", json=payload, headers=headers) as resp:
            data = await resp.json()
            print(f"Статус: {resp.status}")
            print(data)


if __name__ == "__main__":
    asyncio.run(main())
