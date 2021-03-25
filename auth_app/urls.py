from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView

from auth_app.forms import ClientCreationForm
from auth_app.views import AccountCabinet, CabinetOrderDetail


app_name = 'auth_app'
urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='auth_app/login.html'),
        name='login'),

    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

    path('register/', CreateView.as_view(
        template_name='auth_app/register.html',
        form_class=ClientCreationForm,
        success_url='/'),
        name='register'),

    path('cabinet/<pk>/',AccountCabinet.as_view(template_name='auth_app/cabinet.html'), name='cabinet'),
    path('orders/<pk>)/<cart_id>/',CabinetOrderDetail.as_view(template_name='auth_app/account_order_detail.html'), name='order')
]
