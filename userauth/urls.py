from django.urls import path
from . import views

app_name = 'userauth'
urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('login/', views.user_login, name='login'),
    path('select-business/', views.select_business, name='select-business'),
    path('logout/', views.user_logout, name='logout'),
]