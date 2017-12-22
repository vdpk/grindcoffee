from django.conf.urls import url
from catalog.views import (
    ProductDetailView,
    ProductCategoryListView
    )


urlpatterns = [
    url(r'^category/(?P<category_id>\d+)/', ProductCategoryListView.as_view(), name='category'),
    url(r'^(?P<product_id>\d+)/', ProductDetailView.as_view(), name='detail'),
]
