from django.contrib import admin
from . models import BrushBazaarProducts, Categories
# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    search_fields = ['product', 'artist', 'description', 'category__category']
    list_display = ['product', 'artist', 'category', 'stock', 'price']
    list_editable = ['stock', 'price']
admin.site.register(BrushBazaarProducts, ItemAdmin)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"link":['category',]}
admin.site.register(Categories, CategoryAdmin)

