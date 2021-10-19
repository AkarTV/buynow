from django.urls import path
from . import views

urlpatterns = [
    #Category real estate main page (list of ads)
    path('', views.real_estate, name='real_estate'),
    #The real estate ad creation page
    path('create_real_estate/', views.create_real_estate, name='create_real_estate'),
    #The page of the curent ad view
    path('<int:real_estate_id>/', views.show_real_estate_ad, name='show_real_estate_ad'),
    #The real estate ad editing page
    path('edit_real_estate/<int:real_estate_id>/', views.edit_real_estate_ad, name='edit_real_estate_ad'),
]