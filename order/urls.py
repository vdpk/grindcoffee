from django.conf.urls import url
from django.views.generic import TemplateView
from order.views import (
    OrderDetail,
    order_product

    )


urlpatterns = [
    # url(r'^(?P<user_id>[0-9]+)/(?P<cart_id>[0-9]+)/$', order_product, name='detail'),
    url(r'^$', order_product, name='detail'),
    url(r'^(?P<user_id>\d+)/(?P<cart_id>\d+)/$', order_product, name='detail'),
]
