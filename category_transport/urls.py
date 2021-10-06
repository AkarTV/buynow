from django.urls import path
from . import views

urlpatterns = [
    path('', views.transport, name='transport'),
    #Create transport ad
    path('create_transport/', views.create_transport, name='create_transport'),
    path('<int:transport_id>/', views.show_transport_ad, name='show_transport_ad'),
]