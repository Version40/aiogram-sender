from aiogram.types import Message
from core.utils.dbconnect import Request


async def get_start(message: Message, request: Request):
    await request.add_data(message.from_user.id, message.from_user.first_name, message.from_user.last_name)
    await message.answer(f'Привіт {message.from_user.first_name}. Радий тебе бачити! Обери необхідну команду.')
