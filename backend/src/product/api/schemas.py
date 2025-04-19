from pydantic import BaseModel

class ReadProductSchema(BaseModel):
    id: int
    name: str
    category_id: int

    class Config:
        from_attributes = True

class CreateProductSchema(BaseModel):
    name: str
    category_id: int