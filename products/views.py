from django.shortcuts import render
from products.models import Product, ProductCategory


def index(requests):
    context = {'title': 'PatriotStore'}
    return render(requests, 'products/index.html', context)


def products(requests):
    context = {
                'title': 'Products',
                'products': Product.objects.all(),
                'categories': ProductCategory.objects.all()
    }
    return render(requests, 'products/product.html',context)