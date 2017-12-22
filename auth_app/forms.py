from django.contrib.auth.forms import UserCreationForm

from auth_app.models import ClientUser

class ClientCreationForm(UserCreationForm):
    class Meta:
        model = ClientUser
        fields = ('username','first_name','last_name')
