# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number")

class Business(models.Model):
    BUSINESS_TYPES = [
        ('shop', 'Shop'),
        ('restaurant', 'Restaurant'),
        ('pharmacy', 'Pharmacy'),
        ('butchery', 'Butchery'),
        ('bar', 'Bar'),
        ('outfits', 'Outfits'),
        ('grocery', 'Grocery'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="businesses")
    name = models.CharField(max_length=100)
    tin_number = models.CharField(max_length=20, unique=True, verbose_name='TIN Number', default='000000000')
    business_type = models.CharField(max_length=20, choices=BUSINESS_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
