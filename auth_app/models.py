from django.contrib.auth.models import AbstractUser
from django.db import models


class ClientUser(AbstractUser):
    comment_note = models.CharField(max_length=120, blank=True)








