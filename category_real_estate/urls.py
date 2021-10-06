from django.urls import path
from . import views

urlpatterns = [
    path('', views.real_estate, name='real_estate'),
    #Create real estate ad
    path('create_real_estate/', views.create_real_estate, name='create_real_estate'),
    path('<int:real_estate_id>/', views.show_real_estate_ad, name='show_real_estate_ad'),
]