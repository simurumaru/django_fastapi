from fastapi import APIRouter
from product.models import Product
from product.api.schemas import CreateProductSchema, ReadProductSchema

router = APIRouter()

@router.get(
    "/products",
    response_model=list[ReadProductSchema]
)
def list_categories():
    products = Product.objects.all()
    return [ReadProductSchema.model_validate(product) for product in products]

@router.post(
    "/products",
    response_model=ReadProductSchema
)
def create_category(data: CreateProductSchema):
    category = Product.objects.create(**data.dict())
    return category
