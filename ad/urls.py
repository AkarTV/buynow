from django.urls import path
from . import views

urlpatterns = [
    #Домашняя страница
    path('', views.main, name='main'),
    #Каталог транспорта
    path('transport/', views.transport, name='transport'),
    #Каталог недвижимости
    path('real_estate/', views.real_estate, name='real_estate'),
    #Каталог другое
    path('other/', views.other, name='other'),
    #Создать объявление с категорией "другое"
    path('create_other/', views.create_other, name='create_other'),
]