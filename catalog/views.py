from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Product, ProductVariant


class ProductCategoryListView(ListView):
    template_name = 'catalog/product_category_list.html'
    queryset = Product.objects.select_related().select_related().all()

    def get_context_data(self, *args, **kwargs):
        context = super(ProductCategoryListView, self).get_context_data(*args, **kwargs)
        context['products'] = ProductCategoryListView.queryset.filter(product_type__category_id=self.kwargs.get("category_id"))
        return context



class ProductDetailView(DetailView):
    queryset = Product.objects.all()

    def get_object(self, queryset=queryset):
        product_id = self.kwargs.get("product_id")
        obj = get_object_or_404(Product, pk=product_id)
        return obj

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args,**kwargs)
        context['product_variants'] = ProductVariant.objects.filter(product=self.kwargs.get('product_id'))
        print(context)
        return context
