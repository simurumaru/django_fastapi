from fastapi import APIRouter
from category.models import Category
from category.api.schemas import CreateCategorySchema, ReadCategorySchema

from asgiref.sync import sync_to_async

router = APIRouter()

@router.get(
    "/categories",
)
async def list_categories() -> list[ReadCategorySchema]:
    categories = await sync_to_async(list)(Category.objects.all())
    return [ReadCategorySchema.model_validate(category) for category in categories]

@router.post(
    "/categories",
)
async def create_category(data: CreateCategorySchema) -> ReadCategorySchema:
    category = await sync_to_async(Category.objects.create)(**data.model_dump())
    return ReadCategorySchema.model_validate(category)
