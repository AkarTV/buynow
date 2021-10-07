from django.urls import path
from . import views

urlpatterns = [
    #Home page
    path('', views.main, name='main'),
    #Category selection page
    path('choose_category/', views.choose_category, name='choose_category'),
    #Ad view page
    path('show_ad/<str:category>/<int:ad_id>/', views.show_ad_from_main, name='show_ad'),
]