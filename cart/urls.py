from django.conf.urls import url
from django.views.generic import TemplateView
from cart.views import get_cart, add_to_cart, remove_from_cart, ItemInCart ,set_cart_to_order


urlpatterns = [
    url(r'^(?P<user_id>\d+)/$', get_cart, name='get'),
    url(r'^add/(?P<product_id>\d+)/(?P<quantity>\d+)/$', add_to_cart, name='add'),
    url(r'^remove/(?P<product_id>\d+)/$', remove_from_cart, name='remove'),
    url(r'^set/(?P<user_id>\d+)/(?P<cart_id>\d+)/$', set_cart_to_order, name='set'),
    # url(r'^set/$', set_checked_out_to_cart, name='set'),
    # url(r'order/', OrderView.as_view(template_name = 'cart/order.html'), name='orderpage'),
    url(r'^show/(?P<pk>\d+)/$', ItemInCart.as_view(template_name='cart/items.html'), name='show'),
]
