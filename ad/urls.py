from django.urls import path
from . import views

urlpatterns = [
    #Домашняя страница
    path('', views.main, name='main'),
    path('choose_category/', views.choose_category, name='choose_category'),
    path('show_ad/<str:category>/<int:ad_id>/', views.show_ad, name='show_ad'),
]