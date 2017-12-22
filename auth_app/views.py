from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from order.models import ProductOrder
from .models import ClientUser
from cart.models import Item


class AccountCabinet(LoginRequiredMixin, DetailView):
    """
    Личный кабинет с заказами
    """
    login_url = '/auth/login'
    model = ClientUser


    def get_context_data(self, *args, **kwargs):
        context = super(AccountCabinet, self).get_context_data(*args, **kwargs)
        context['orders'] = ProductOrder.objects.filter(customer_id=self.kwargs.get('pk'))
        return context


class CabinetOrderDetail(DetailView):
    """
    Информация по заказу
    """
    model = Item

    def get_context_data(self, *args, **kwargs):
        context = super(CabinetOrderDetail, self).get_context_data(*args, **kwargs)
        context['order'] = ProductOrder.objects.get(pk=self.kwargs.get('pk'))
        context['items'] = Item.objects.filter(cart=self.kwargs.get('cart_id'))
        return context