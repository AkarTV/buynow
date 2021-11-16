from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm

def register(request):
    '''Register new user'''
    if request.method != 'POST':
        base_form = UserCreationForm()
    else:
        base_form = UserCreationForm(data = request.POST)
        if base_form.is_valid():
            new_user = base_form.save()
            login(request, new_user)   
            return redirect('main')
    context = {'form': base_form}
    return render(request, 'registration/registration.html', context)

def profile_page(request):
    '''Return the page of the user profile'''
    current_user = request.user
    return render(request, 'registration/profile_page.html', {'user': current_user})

def edit_profile(request):
    '''Return the user profie editing page'''
    if request.method != 'POST':
        user_form = UserForm(instance=request.user)
    else:
        user_form = UserForm(request.POST, request.FILES, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('profile')
    context = {'user_form': user_form}
    return render(request, 'registration/edit_profile.html', context)
    

def password_succes(request):
    return render(request, 'registration/password_succes.html')