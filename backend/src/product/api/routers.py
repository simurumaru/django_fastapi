from fastapi import APIRouter
from product.models import Product
from product.api.schemas import CreateProductSchema, ReadProductSchema

from asgiref.sync import sync_to_async

router = APIRouter()

@router.get(
    "/products",
)
async def list_products() -> list[ReadProductSchema]:
    products = await sync_to_async(list)(Product.objects.all())
    return [ReadProductSchema.model_validate(product) for product in products]

@router.post(
    "/products",
)
async def create_product(data: CreateProductSchema) -> ReadProductSchema:
    product = await sync_to_async(Product.objects.create)(**data.model_dump())
    return ReadProductSchema.model_validate(product)
