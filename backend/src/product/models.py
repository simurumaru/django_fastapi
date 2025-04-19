from django.db import models
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=35)
    category = models.ForeignKey(
        'category.Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
