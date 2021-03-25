from django.urls import path
from order.views import order_product


app_name = 'order'
urlpatterns = [
    path('<user_id>/<cart_id>/', order_product, name='detail')
]
