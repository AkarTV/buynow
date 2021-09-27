from django.urls import path
from . import views

urlpatterns = [
    #Домашняя страница
    path('', views.main, name='main'),
]