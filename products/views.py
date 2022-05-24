from django.shortcuts import render


def index(requests):
    return render(requests, 'products/index.html')


def products(requests):
    return render(requests, 'products/product.html')