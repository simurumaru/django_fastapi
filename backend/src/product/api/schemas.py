from core.schemas.base import PublicSchema, ORMSchema

class ReadProductSchema(ORMSchema):
    id: int
    name: str
    category_id: int

class CreateProductSchema(PublicSchema):
    name: str
    category_id: int
