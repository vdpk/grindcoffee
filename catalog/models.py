from django.db import models
from django.db.models import Manager


class ProductAvailableManager(Manager):
    # Только доступные товары
    def get_queryset(self, **kwargs):
        return super().get_queryset().filter(
            is_available=True
        )



class Product(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=400, null=True)
    weight = models.CharField(max_length=50, null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    quantity = models.PositiveIntegerField(verbose_name='quantity')
    is_available = models.BooleanField(default=True)

    has_variants = models.BooleanField(default=False)

    product_type = models.ForeignKey('ProductType', related_name='products')

    objects = Manager()
    available_objects = ProductAvailableManager()

    def __str__(self):
        return self.name

#
#     пока не реализовано - варианты товаров по весу
#
# class ProductVariant(models.Model):
#
#     product = models.ForeignKey('Product', related_name='product_vars')
#     weight_override = models.ForeignKey('ProductWeight', related_name='product_variants')
#     name = models.CharField(max_length=50)
#     price_override = models.DecimalField(max_digits=10, decimal_places=2, null=True)
#
#
#     objects = Manager()
#
#     def __str__(self):
#         return self.name


class ProductWeight(models.Model):
    # вес тип
    weight = models.CharField(max_length=10)

    def __str__(self):
        return '{} g'.format(self.weight)


class ProductType(models.Model):
    # тип продукта (например, арабика)
    title = models.CharField(max_length=50)

    category = models.ForeignKey('Category', related_name='product_type')

    def __str__(self):
        return self.title


class Category(models.Model):
    # категория товара (например, кофе)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title





















































#
# class Product(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField(max_length=400, null=True)
#
#     size_variants = models.BooleanField(default=True)
#
#
#
#     type = models.ForeignKey('ProductType', related_name='products')
#
#     size = models.ForeignKey('ProductPackageSize', related_name='products')
#
#     price =
#     is_available = models.BooleanField(default=True)
#
#
#
#
#
# class IsAvailableManager(models.Manager):
#     def get_queryset(self,**kwargs):
#         return super().get_queryset().filter(
#             is_available=True,
#         )
#
#
# class ProductSize(models.Model):
#     SMALL = ('S', '250g')
#     MEDIUM = ('M', '500g')
#     LARGE = ('L', '1kg')
#
#     __sizes = dict([SMALL, MEDIUM, LARGE])
#
#     product_size = models.CharField(max_length=1, choices=__sizes.items())
#
#     def __str__(self):
#         return str(self.__sizes[self.product_size])
#
#
# class ProductType(models.Model):
#     title = models.CharField(max_length=50)
#     category = models.ForeignKey('Category', related_name='+')
#
#
#
#
#
#
#
#
# class Product(models.Model):
#
#     name = models.CharField(max_length=120)
#     description = models.TextField(max_length=500, null=True)
#     product_type = models.ForeignKey('ProductType', related_name='product_type')
#
#
#     price = models.DecimalField(max_digits=10,decimal_places=2)
#     is_available = models.BooleanField(default=True)
#
#     def __str__(self):
#         return self.name
#
#     @property
#     def price(self):
#         return "RUB%s" % self.price
#
#     objects = Manager()
#     available_object = IsAvailableManager()
#
#
# class Category(models.Model):
#     title = models.CharField(max_length=100)
#
#     objects = Manager()
#
#     def __str__(self):
#         return self.title
#
# #
# # class ProductWeight(models.Model):
# #     SMALL = ('S', 'Small')
# #     MEDIUM = ('M', 'Medium')
# #     LARGE = ('L', 'Large')
# #     EXTRA_LARGE = ('XL','Extra Large')
# #     __all = dict([SMALL, MEDIUM, LARGE, EXTRA_LARGE])
# #
# #     size_shortcut = models.CharField(max_length=2, choices=__all.items())
# #     size_weight = models.IntegerField(max_length=3, choices= v[3] in __all.items())
# #
#
#
#
#

