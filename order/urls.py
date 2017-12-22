from django.conf.urls import url
from order.views import order_product



urlpatterns = [
    url(r'^(?P<user_id>\d+)/(?P<cart_id>\d+)/$', order_product, name='detail')
]
