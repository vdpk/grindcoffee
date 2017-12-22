from django.contrib import admin
from .models import ClientUser


class ClientUserAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'username',
                    'first_name',
                    'last_name',
                    'comment_note',)

    search_fields = ('id',
                     'username',)


admin.site.register(ClientUser, ClientUserAdmin)