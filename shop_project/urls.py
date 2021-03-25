from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='catalog/home_page.html'), name='home'),
    path('catalog/', include('catalog.urls', namespace='catalog')),
    path('account/', include("auth_app.urls", namespace='account')),
    path('cart/', include("cart.urls", namespace='cart')),
    path('order/', include("order.urls", namespace='order'))
]
