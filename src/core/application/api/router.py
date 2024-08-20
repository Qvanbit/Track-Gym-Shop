from fastapi import APIRouter


router = APIRouter(
    prefix="/main",
    tags=['main']
)

@router.get("/", 
            description='Проверяет работу приложения, в случае корректного запуска возвращает сообщение "all good"',
            )
async def check_work_app():
    return {"message": "All good"}