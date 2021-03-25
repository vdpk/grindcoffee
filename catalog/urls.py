from django.urls import path
from catalog.views import (ProductDetailView, ProductCategoryListView)

app_name = 'catalog'
urlpatterns = [
    path('category/<category_id>/', ProductCategoryListView.as_view(), name='category'),
    path('<product_id>/', ProductDetailView.as_view(), name='detail'),
]
