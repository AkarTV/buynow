from django.shortcuts import render
from . models import Ad, Real_Estate_Ad, Other_Ad, Transport_Ad
from itertools import chain
from operator import attrgetter

#Главная страница
def main(request):  
    transport = Transport_Ad.objects.all()
    houses = Real_Estate_Ad.objects.all()
    other = Other_Ad.objects.all() 
    result = sorted(chain(transport, houses, other), key=attrgetter('date'), reverse=True)
    context = {'ads': result}
    return render(request, 'ad/main.html', context)

#Страница с транспортом
def transport(request):
    transport = Transport_Ad.objects.order_by('-date')
    context = { 'ads' : transport}
    return render(request, 'ad/transport.html', context)

#Страница с недвижимостью
def real_estate(request):
    houses = Real_Estate_Ad.objects.order_by('-date')
    context = { 'ads' : houses }
    return render(request, 'ad/real_estate.html', context)
#Страница с каталогом "Другое"
def other(request):
    other = Other_Ad.objects.order_by('-date')
    context = { 'ads' : other }
    return render(request, 'ad/other.html', context)
#
def create_other(request):
    context = {}
    return render(request, 'ad/create_other.html', context)