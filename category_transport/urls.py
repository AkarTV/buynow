from django.urls import path
from . import views

urlpatterns = [
    #Category transport main page (list of ads)
    path('', views.transport, name='transport'),
    #Transport ad creation page
    path('create_transport/', views.create_transport, name='create_transport'),
    #The page of the curent ad view
    path('<int:transport_id>/', views.show_transport_ad, name='show_transport_ad'),
    #Transport ad editing page
    path('edit_transport/<int:transport_id>/', views.edit_transport_ad, name='edit_transport_ad'),
]