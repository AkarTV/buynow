
from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('registration/', views.register, name='registration'),
    path('profile/', views.profile_page, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
] 