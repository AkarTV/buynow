from django.urls import path
from . import views

urlpatterns = [
    path('', views.other, name='other'),
    #Создать объявление с категорией "другое"
    path('create_other/', views.create_other, name='create_other'),
]