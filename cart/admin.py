from django.contrib import admin
from .models import Cart, Item
# Register your models here.



class CartAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'creation_date',
                    'checked_out',)

    list_filter = ('checked_out',)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('cart',
                    'product',
                    'quantity',
                    'unit_price',)

    list_display_links = ('cart',)

    list_filter = ('cart', )


admin.site.register(Cart, CartAdmin)
admin.site.register(Item, ItemAdmin)
