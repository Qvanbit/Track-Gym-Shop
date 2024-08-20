from fastapi import APIRouter, Depends



router = APIRouter(
    prefix="/operations",
    tags=['Operations'],
)


@router.get("/re")
async def get_operations(session: AsyncSession = Depends(get_async_session)):
    