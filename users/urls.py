from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registration/', views.register, name='registration'),
    path('profile/', views.profile_page, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('password-change/', auth_views.PasswordChangeView.as_view(success_url = 'password_succes'), name='password_change'),
    path('password-change/password_succes/', views.password_succes, name='password_succes'),
] 