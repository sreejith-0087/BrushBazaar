from django.contrib import admin
from .models import CustomerDetails
# Register your models here.



@admin.register(CustomerDetails)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email', 'address']
    search_fields = ['first_name', 'last_name', 'phone', 'email']


