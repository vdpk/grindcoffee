from django.conf.urls import url
from cart.views import get_cart, add_to_cart, remove_from_cart ,redirect_to_order


urlpatterns = [
    url(r'^(?P<user_id>\d+)/$', get_cart, name='get'),
    url(r'^add/(?P<product_id>\d+)/(?P<quantity>\d+)/$', add_to_cart, name='add'),
    url(r'^remove/(?P<product_id>\d+)/$', remove_from_cart, name='remove'),
    url(r'^set/(?P<user_id>\d+)/(?P<cart_id>\d+)/$', redirect_to_order, name='set')
]
