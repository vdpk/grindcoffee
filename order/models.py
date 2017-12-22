from django.db import models
import datetime

class ProductOrder(models.Model):
    customer_id = models.CharField(max_length=120)

    cart_id = models.CharField(max_length=120, default=None)


    address = models.CharField(max_length=450, verbose_name='Укажите свой адрес')
    delivery_time = models.CharField(max_length=122, verbose_name= 'Желаемое время доставки')
    comment = models.CharField(max_length=400, verbose_name='Комментарий')

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        hr_created_time = datetime.datetime.strptime(str(self.created_date)[:10], '%Y-%m-%d').strftime('%d-%m-%Y')
        return 'Заказ #{} от {}'.format(self.pk, hr_created_time)

