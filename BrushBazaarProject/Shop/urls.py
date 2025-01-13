from django.urls import path
from . views import *

app_name = 'Shop'

urlpatterns = [
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('shop/', Shop, name='shop'),
    path('category/<slug:link>', Shop, name='by_category'),
]

