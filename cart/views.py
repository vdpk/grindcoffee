# Create your views here.
from cart.cart import Cart
from cart.models import Cart as CartModel, Item
from catalog.models import Product
from django.shortcuts import render_to_response, HttpResponseRedirect, HttpResponse, render, redirect
from django.views.generic import ListView
from django.contrib import messages

from django.views.generic.edit import FormView
from auth_app.models import ClientUser

from django.urls import reverse
from django.http import request

from order.views import order_product

def add_to_cart(request, product_id, quantity):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product, product.price, quantity)
    messages.add_message(request, messages.INFO, "Добавлено")
    return HttpResponseRedirect(redirect_to='/catalog/{}'.format(product_id))

def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    try:
        cart.remove(product)
        messages.add_message(request, messages.INFO, "Удалено")
    except Exception:
        messages.add_message(request, messages.INFO, "Товара не существует в корзине")
        pass
    return HttpResponseRedirect(redirect_to='/catalog/{}'.format(product_id))

def get_cart(request, user_id):
    user_info = ClientUser.objects.get(pk=user_id)
    print(user_info.username)
    print(user_info.id)
    cart_context = Cart(request)

    check_item = Item.objects.filter(cart=Cart(request).cart.pk)
    print(len(check_item))
    if check_item == []:
        print('Op')
    print(check_item)
    print(cart_context.cart.pk)
    # c = {
    #     'user': user_info,
    #     'cart': cart_context,
    # }
    # print(cart_context)
    return render_to_response('cart/cart.html',{'cart': Cart(request), 'user': user_info, 'check_item_state': check_item})



def set_cart_to_order(user_id, cart_id):
    return redirect(reverse('order:detail', kwargs={'user_id': user_id, 'cart_id': cart_id}))


def order_create(request):
    if request.method == 'POST':
        cart_order = Cart(request)


class ItemInCart(ListView):
    model = Item
    # print(queryset)

    def get_context_data(self, *args, **kwargs):
        context = super(ItemInCart,self).get_context_data(*args,**kwargs)
        context['items'] = Item.objects.all()
        # object_id = context
        # context['products'] = Product.objects.get(pk = pk)

        return context

#
# class OrderView(FormView):
#     template_name = 'cart/order.html'
#     form_class = OrderForm
#     success_url = '/'
#

























