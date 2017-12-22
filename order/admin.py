from django.contrib import admin
from order.models import ProductOrder
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'customer_id',
                    'cart_id',
                    'created_date')

    list_filter = ('customer_id',
                    'cart_id')



admin.site.register(ProductOrder, OrderAdmin)