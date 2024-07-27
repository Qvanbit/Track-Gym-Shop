from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command
import httpx

from src.bot.messages.start import StartMessageBuilder


start_handler_router = Router()
FASTAPI_URL = 'http://main-app:8000'

@start_handler_router.message(CommandStart())
async def start(message: types.Message) -> None:
    await message.answer('Привет! Это бот для управления чеками.')
    
@start_handler_router.message(Command('menu'))
async def echo(message: types.Message) -> None:
    ...
    

async def fetch_message_from_fastapi():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{FASTAPI_URL}/")
        if response.status_code == 200:
            return response.json().get("message", "No message")
        else:
            return "Error contacting API"

@start_handler_router.message(lambda message: message.text.lower() == 'test')
async def send_test_response(message: types.Message):
    api_message = await fetch_message_from_fastapi()
    await message.reply(api_message)
    
@start_handler_router.message(F.text)
async def menu_cmd(message: types.Message) -> None:
    await message.answer('It is a magick method')
    