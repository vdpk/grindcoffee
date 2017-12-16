from django.conf.urls import url

from django.contrib.auth.views import logout_then_login, LoginView
from django.views.generic import CreateView

from auth_app.forms import ClientCreationForm



urlpatterns = [
    url(r'^login/', LoginView.as_view(
        template_name='auth_app/login.html'
    ), name='login'),

    url(r'^logout/', logout_then_login, name='logout'),

    url(r'^register/', CreateView.as_view(
        template_name='auth_app/register.html',
        form_class=ClientCreationForm,
        success_url='/'
    ), name='register')
]
