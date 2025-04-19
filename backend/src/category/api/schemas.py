from pydantic import BaseModel

class ReadCategorySchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class CreateCategorySchema(BaseModel):
    name: str