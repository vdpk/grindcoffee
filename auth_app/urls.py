from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView

from auth_app.forms import ClientCreationForm
from auth_app.views import AccountCabinet, CabinetOrderDetail



urlpatterns = [
    url(r'^login/', LoginView.as_view(
        template_name='auth_app/login.html'),
        name='login'),

    url(r'^logout/', LogoutView.as_view(next_page='/'), name='logout'),

    url(r'^register/', CreateView.as_view(
        template_name='auth_app/register.html',
        form_class=ClientCreationForm,
        success_url='/'),
        name='register'),

    url(r'^cabinet/(?P<pk>\d+)/$',AccountCabinet.as_view(template_name='auth_app/cabinet.html'), name='cabinet'),
    url(r'^orders/(?P<pk>\d+)/(?P<cart_id>\d+)/',CabinetOrderDetail.as_view(template_name='auth_app/account_order_detail.html'), name='order')
]
