from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from src.bot.messages.base import BaseMessageBuilder


class StartMessageBuilder(BaseMessageBuilder):
    _text = "/menu"
    _reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="1️⃣ Добавить друга", callback_data="friend")],
            [InlineKeyboardButton(text="2️⃣ Разбить чек", url="https://ya.ru")],
        ],
    )
