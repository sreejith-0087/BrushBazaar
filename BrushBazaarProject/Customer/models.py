from django.db import models
from django.contrib.auth.models import User
from Shop.models import BrushBazaarProducts
# Create your models here.


class CustomerDetails(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.BigIntegerField(unique=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='Customers/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Feedback(models.Model):
    user = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE)
    feedback = models.TextField()
    product = models.ForeignKey(BrushBazaarProducts, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

