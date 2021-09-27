from django.urls import path
from . import views

urlpatterns = [
    path('', views.real_estate, name='real_estate'),
]