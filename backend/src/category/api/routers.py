from asgiref.sync import sync_to_async
from fastapi import APIRouter
from category.models import Category
from category.api.schemas import CreateCategorySchema, ReadCategorySchema

router = APIRouter()

@router.get(
    "/categories",
    response_model=list[ReadCategorySchema]
)
def list_categories():
    categories = Category.objects.all()
    return [ReadCategorySchema.model_validate(category) for category in categories]

@router.post(
    "/categories",
    response_model=ReadCategorySchema
)
def create_category(data: CreateCategorySchema):
    category = Category.objects.create(**data.model_dump())
    return category
