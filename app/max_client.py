"""Минимальный асинхронный клиент MAX Bot API — только то, что нужно для примера."""

import logging

import aiohttp

logger = logging.getLogger("max_bot_template")


class MaxClient:
    def __init__(self, token: str, base_url: str):
        self.token = token
        self.base_url = base_url

    def _headers(self) -> dict:
        return {"Authorization": self.token, "Content-Type": "application/json"}

    async def send_message(self, chat_id: int, text: str) -> dict | None:
        """Отправляет сообщение. Возвращает None при ошибке — не роняет обработчик апдейта."""
        url = f"{self.base_url}/messages"
        params = {"chat_id": chat_id}
        payload = {"text": text}
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, params=params, json=payload, headers=self._headers()) as resp:
                    if resp.status != 200:
                        body_text = await resp.text()
                        logger.error(f"Ошибка отправки в chat_id={chat_id}: {resp.status} — {body_text}")
                        return None
                    return await resp.json()
        except aiohttp.ClientError as e:
            logger.error(f"Сетевая ошибка send_message: {e}")
            return None
