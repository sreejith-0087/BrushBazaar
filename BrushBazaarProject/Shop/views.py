from itertools import product

from django.shortcuts import render, redirect
from . models import Categories, BrushBazaarProducts
from django.core.paginator import Paginator
from django.db.models import Q
from Customer.models import Feedback
# Create your views here.


def Home(request):
    products = BrushBazaarProducts.objects.all()
    product = products[:3]
    return render(request, 'Home/Index.html', {'product': product})

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
        paginator = Paginator(all_items, 9)
        page_number = request.GET.get('page')
        products = paginator.get_page(page_number)
    return render(request, 'Shop/Shop.html', {'products': products})


def Product_Search(request):
    query = request.GET.get('q')
    if query:
        result = BrushBazaarProducts.objects.all().filter(Q(product__icontains=query)|
                                                    Q(category__category__icontains=query)|
                                                    Q(artist__icontains=query))
    else:
        result = []

    return render(request, 'Shop/Shop.html', {'products': result})


def Single_Product(request, pro_id):
    brushbazaarsingle = BrushBazaarProducts.objects.get(id=pro_id)
    feedback_list = Feedback.objects.filter(product=pro_id).order_by('-created_at')
    return render(request, 'Shop/Shop_Single.html', {'pro': brushbazaarsingle, 'feedback_list': feedback_list})