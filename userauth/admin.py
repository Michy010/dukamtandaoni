from django.contrib import admin
from . models import CustomUser, Business

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Business)