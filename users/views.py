from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm, CustomerForm

def register(request):
    '''Register new user'''
    if request.method != 'POST':
        base_form = UserCreationForm()
        extend_form = UserForm()
        custom_form = CustomerForm()
    else:
        base_form = UserCreationForm(data = request.POST)
        extend_form = UserForm(data = request.POST)
        custom_form = CustomerForm(data= request.POST)
        if base_form.is_valid() and extend_form.is_valid() and custom_form.is_valid():
            new_user = base_form.save()
            extend_form.save()
            custom_form.save()
            login(request, new_user)    
            return redirect('main')
    context = {'form': base_form, 'extend_form': extend_form, 'custom_form': custom_form}
    return render(request, 'registration/registration.html', context)

def profile_page(request):
    '''Return the page of the user profile'''
    current_user = request.user
    return render(request, 'registration/profile_page.html', {'user': current_user})

def edit_profile(request):
    '''Return the user profie editing page'''
    if request.method != 'POST':
        extend_form = UserForm(instance=request.user)
        custom_form = CustomerForm(instance=request.user.customer)
    else:
        extend_form = UserForm(data=request.POST)
        custom_form = CustomerForm(data=request.POST)
        if extend_form.is_valid() and custom_form.is_valid():
            extend_form.save()
            custom_form.save()
            return redirect('profile')
    context = {'extend_form': extend_form, 'custom_form': custom_form}
    return render(request, 'registration/edit_profile.html', context)