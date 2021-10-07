from django.urls import path
from . import views

urlpatterns = [
    #Category other main page (list of ads)
    path('', views.other, name='other'),
    #The other ad creation page
    path('create_other/', views.create_other, name='create_other'),
    #The page of the curent ad view
    path('<int:category_other_id>/', views.show_other_ad, name='show_other_ad'),
]