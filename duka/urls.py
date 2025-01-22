from django.urls import path
from . import views

app_name ='duka'
urlpatterns = [
    path('', views.index, name='home'),
]