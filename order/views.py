from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.db import transaction
# Create your views here.

from order.forms import OrderForm
from order.models import ProductOrder
from cart.models import Cart as CartModel


def order_product(request, user_id, cart_id):
    if request.method=='GET': # отображаем форму
        c = {
            'customer': user_id,
            'cart': cart_id,
            'order_form': OrderForm(),
        }

        return render(request, 'order/order_detail.html',c)

    elif request.method=='POST': # забираем данные из формы и сохраняем в модель
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            with transaction.atomic():
                order = ProductOrder(
                    customer_id=user_id,
                    cart_id=cart_id,
                    address = order_form.cleaned_data['address'],
                    delivery_time = order_form.cleaned_data['delivery_time'],
                    comment = order_form.cleaned_data['comment']
                )
                order.save()
                cart = CartModel.objects.get(pk=cart_id)
                cart.set_check_out()

            return HttpResponseRedirect('/')
    else:
        print('Not Valid')

    return HttpResponse(status=405)