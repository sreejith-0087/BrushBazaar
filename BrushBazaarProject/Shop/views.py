from itertools import product

from django.shortcuts import render, redirect
from unicodedata import category

from . models import Categories, BrushBazaarProducts
from django.core.paginator import Paginator
# Create your views here.


def Home(request):
    return render(request, 'Home/Index.html')

def About(request):
    return render(request, 'Home/About.html')

def Contact(request):
    return render(request, 'Home/Contact.html')

def Shop(request, link=None):
    if link is not None:
        cat = Categories.objects.get(link=link)
        products = BrushBazaarProducts.objects.filter(category=cat.id)
    else:
        all_items = BrushBazaarProducts.objects.all()
        paginator = Paginator(all_items, 30)
        page_number = request.GET.get('page')
        products = paginator.get_page(page_number)
    return render(request, 'Shop/Shop.html', {'products': products})


