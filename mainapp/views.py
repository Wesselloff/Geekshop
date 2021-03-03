from django.shortcuts import render
from mainapp.models import Product, ProductCategory
import os
import json
from datetime import datetime

folder = os.path.dirname(__file__)


# Create your views here.
def index(request):
    context = {
        'title': 'geekshop',
        'header': 'GeekShop Store',
        'text': 'Новые образы и лучшие бренды на GeekShop Store. Бесплатная доставка по всему миру! '
                'Аутлет: до -70% Собственный бренд. -20% новым покупателям.'
    }
    return render(request, 'mainapp/index.html', context)


def products(request, id=None):
    context = {
        'title': 'GeekShop - Каталог',
        'year': datetime.now(),
        'prods': Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }

    # file_path = os.path.join(folder, 'fixtures/products.json')
    # with open(file_path, 'r', encoding='utf-8') as file:
    #     context.update(json.load(file))
    return render(request, 'mainapp/products.html', context)
