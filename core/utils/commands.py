from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Запустити бота'
        ),
        BotCommand(
            command='weather',
            description='Погода в місті'
        ),
        BotCommand(
            command='sender',
            description='Розпочати розсилку'
        ),
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())