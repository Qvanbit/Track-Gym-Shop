# import asyncio
# import uvicorn

# from src.core.configs import settings
# from src.bot.bot import main as setup_telegram_bot
# from src.core.application.api.main import create_app


# async def start_fastapi():
#     app = create_app()
#     config = uvicorn.Config(app, host="0.0.0.0", port=settings.FAST_API_PORT, log_level="info")
#     server = uvicorn.Server(config)
#     await server.serve()


# async def main():
#     # Создаем задачи для запуска бота и FastAPI
#     bot_task = asyncio.create_task(setup_telegram_bot())
#     fastapi_task = asyncio.create_task(start_fastapi())

#     # Ожидаем завершения обеих задач
#     await asyncio.gather(bot_task, fastapi_task)


# if __name__ == "__main__":
#     asyncio.run(main())
