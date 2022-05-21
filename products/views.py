from django.shortcuts import render


def index(requests):
    return render(requests, 'products/index.html')
