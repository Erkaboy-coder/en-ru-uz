import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5767247528:AAFpLJojT6-RVYrDGqV2WztFaUidb3qZRbY'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
