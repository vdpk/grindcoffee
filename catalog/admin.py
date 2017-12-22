from django.contrib import admin
from .models import Product, ProductType, ProductWeight, Category
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'product_type',
                    'weight',
                    'price',
                    'quantity',
                    )

    list_filter = ('weight',
                   'product_type',
                   'price',)

    list_display_links = ('id',)


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType)
admin.site.register(ProductWeight)
admin.site.register(Category)



