"""
Точка входа: FastAPI-приложение с эндпоинтом вебхука для MAX Bot API.
Запуск: uvicorn app.main:app --host 0.0.0.0 --port 8000
"""

from fastapi import FastAPI, Request

from app.handlers import handle_update

app = FastAPI(title="MAX Bot Template")


@app.get("/")
async def root() -> dict:
    """Проверка, что сервис жив (удобно для healthcheck в Docker/оркестраторе)."""
    return {"status": "ok", "message": "MAX bot template is running"}


@app.post("/webhook")
async def webhook(request: Request) -> dict:
    """Сюда MAX присылает апдейты после регистрации вебхука (см. register_webhook.py)."""
    update = await request.json()
    await handle_update(update)
    return {"ok": True}
