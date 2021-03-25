from django.urls import path
from cart.views import get_cart, add_to_cart, remove_from_cart ,redirect_to_order

app_name = 'cart'
urlpatterns = [
    path('<user_id>/', get_cart, name='get'),
    path('add/<product_id>/<quantity>/', add_to_cart, name='add'),
    path('remove/<product_id>/', remove_from_cart, name='remove'),
    path('set/<user_id>/<cart_id>/', redirect_to_order, name='set')
]
