from .models import ClientUser
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from order.models import ProductOrder

from cart.models import Item

class AccountCabinet(LoginRequiredMixin, DetailView):
    login_url = '/auth/login'
    model = ClientUser
    # queryset = ClientUser.objects.all()
    # print(queryset)
    #
    # def get_object(self, **kwargs):
    #     customer_id = self.pk_url_kwarg


    def get_context_data(self, *args, **kwargs):
        context = super(AccountCabinet, self).get_context_data(*args, **kwargs)
        context['orders'] = ProductOrder.objects.filter(customer_id=self.kwargs.get('pk'))

        # print(context'orders'



        # for i in context['orders']:
        #     order = ProductOrder.objects.get(pk=i.id)
        #     cart = Item.objects.filter(pk = order.cart_id)

            # print(cart.quantity)
        # print(context)
        # print(self.kwargs.get('pk'))
        return context


class CabinetOrderDetail(DetailView):
    # login_url = '/auth/login'
    model = Item

    def get_context_data(self, *args, **kwargs):
        context = super(CabinetOrderDetail, self).get_context_data(*args, **kwargs)
        context['order'] = ProductOrder.objects.get(pk=self.kwargs.get('pk'))
        context['items'] = Item.objects.filter(cart=self.kwargs.get('cart_id'))
        print(context)
        return context