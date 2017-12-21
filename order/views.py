from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.views.generic.edit import FormView
from django.db import transaction
# Create your views here.

from order.forms import OrderForm
from order.models import ProductOrder

from auth_app.models import ClientUser
from cart.models import Cart as CartModel
from django.contrib import messages


class OrderDetail(FormView):
    template_name = 'order/order_detail.html'
    form_class = OrderForm
    success_url = '/'



def order_product(request, user_id, cart_id):
    if request.method=='GET':
        c = {
            # 'user': ClientUser.objects.get(pk=user_id),
            'customer': user_id,
            'cart': cart_id,
            'order_form': OrderForm(),
        }
        print(c)
        # print()
        return render(request, 'order/order_detail.html',c)

    elif request.method=='POST':
        print(user_id, cart_id)
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            print('Valid    ')
            with transaction.atomic():
                print(cart_id, user_id)
                # print(order_form)
                order = ProductOrder(
                    customer_id=user_id,
                    cart_id=cart_id,
                    address = order_form.cleaned_data['address'],
                    delivery_time = order_form.cleaned_data['delivery_time'],
                    comment = order_form.cleaned_data['comment']
                )
                order.save()
                cart = CartModel.objects.get(pk=cart_id)
                print(cart)
                cart.set_check_out()

                print(order)

            return HttpResponseRedirect('/')
    else:
        print('Not Valid')

    return HttpResponse(status=405)