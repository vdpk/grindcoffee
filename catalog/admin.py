from django.contrib import admin
from .models import Product, ProductType, ProductVariant, ProductWeight, Category
# Register your models here.

admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(ProductVariant)
admin.site.register(ProductWeight)
admin.site.register(Category)



