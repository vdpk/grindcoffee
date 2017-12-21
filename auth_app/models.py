from django.contrib.auth.models import AbstractUser
from django.db import models


# from order.models import ProductOrder
# Create your models here.

class ClientUser(AbstractUser):
    comment_note = models.CharField(max_length=120, blank=True)

    # user_orders = models.ForeignKey('ProductOrder', related_name='product_order')

    # user_orders = models.ForeignKey()








