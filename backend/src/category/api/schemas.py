from core.schemas.base import PublicSchema, ORMSchema

class ReadCategorySchema(ORMSchema):
    id: int
    name: str

class CreateCategorySchema(PublicSchema):
    name: str
