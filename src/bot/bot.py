import os

from aiogram import Bot, Dispatcher, types

from src.bot.handlers.start_handler import start_handler_router
from src.bot.settings import ALLOWED_UPDATES
from src.core.configs import settings


bot = Bot(token=settings.TELEGRAM_API_TOKEN)
dispatcher = Dispatcher()

dispatcher.include_routers(
    start_handler_router,
)


async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(
        commands=[],
        scope=types.BotCommandScopeAllPrivateChats(),
    )
    await dispatcher.start_polling(bot, allowed_updates=ALLOWED_UPDATES)
