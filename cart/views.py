# Create your views here.
from cart.cart import Cart
from cart.models import Item
from catalog.models import Product
from django.shortcuts import render_to_response, HttpResponseRedirect, HttpResponse, render, redirect
from django.contrib import messages

from auth_app.models import ClientUser

from django.urls import reverse


def add_to_cart(request, product_id, quantity):
    # добавляем товар в корзину
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product, product.price, quantity)
    messages.add_message(request, messages.INFO, "Добавлено")
    return HttpResponseRedirect(redirect_to='/catalog/{}'.format(product_id))


def remove_from_cart(request, product_id):
    # удаляем товар из корзины
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
    # отображаем информацию по корзине
    user_info = ClientUser.objects.get(pk=user_id)
    check_item = Item.objects.filter(cart=Cart(request).cart.pk)

    return render_to_response('cart/cart.html',{'cart': Cart(request), 'user': user_info, 'check_item_state': check_item})



def redirect_to_order(user_id, cart_id):
    # перекидываем на форму оформления заказа
    return redirect(reverse('order:detail', kwargs={'user_id': user_id, 'cart_id': cart_id}))


























