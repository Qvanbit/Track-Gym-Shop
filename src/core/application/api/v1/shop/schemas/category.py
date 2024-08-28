from pydantic import BaseModel

class GetCategoryListResponseSchema(BaseModel):
    id: int
    name: str

    