from django.urls import path, include
from . import views

urlpatterns = [
    #Home page
    path('', views.main, name='main'),
    #Category selection page
    path('choose_category/', views.choose_category, name='choose_category'),
]