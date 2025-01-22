from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, BusinessRegistrationForm, BusinessSelectionForm
from .models import Business

# Create your views here.
def register(request):
    if request.method == "POST":
        user_form = CustomUserCreationForm(request.POST)
        business_form = BusinessRegistrationForm(request.POST)
        if user_form.is_valid() and business_form.is_valid():
            user = user_form.save()
            business = business_form.save(commit=False)
            business.user = user
            business.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect('userauth:login')
    else:
        user_form = CustomUserCreationForm()
        business_form = BusinessRegistrationForm()
    return render(request, 'userauth/register.html', {'user_form': user_form, 'business_form': business_form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('userauth:select-business')
        messages.error(request, "Invalid credentials.")
    return render(request, 'userauth/login.html')

def select_business(request):
    if request.method == "POST":
        form = BusinessSelectionForm(request.user, request.POST)
        if form.is_valid():
            business = form.cleaned_data['business']
            messages.success(request, f"Welcome to {business.name}!")
            return redirect('dashboard', business_id=business.id)
    else:
        form = BusinessSelectionForm(request.user)
    return render(request, 'userauth/select_business.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('userauth:login')
