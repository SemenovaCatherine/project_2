"""
Модуль для настройки и запуска Telegram-бота.
"""

import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand
from aiogram import Router
from dotenv import load_dotenv
import asyncio

# Загрузка переменных окружения
load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("Токен бота не найден в переменных окружения.")

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
router = Router()

async def set_commands():
    """
    Устанавливает команды для бота.
    """
    commands = [
        BotCommand(command="start", description="Начать работу с ботом"),
        BotCommand(command="help", description="Помощь и описание возможностей"),
    ]
    await bot.set_my_commands(commands)

async def on_startup():
    """
    Выполняется при запуске бота.
    """
    await set_commands()
    logging.info("Бот успешно запущен")

async def main():
    from telegram_bot.handlers import router
    dp.include_router(router)
    await on_startup()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
