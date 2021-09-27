from django.http import request
from django.shortcuts import render, redirect
from category_transport.models import Transport_Ad
from category_real_estate.models import Real_Estate_Ad
from category_other.models import Other_Ad
from itertools import chain
from operator import attrgetter

#Main page
def main(request):  
    transport = Transport_Ad.objects.all()
    houses = Real_Estate_Ad.objects.all()
    other = Other_Ad.objects.all() 
    result = sorted(chain(transport, houses, other), key=attrgetter('date'), reverse=True)
    context = {'ads': result}
    return render(request, 'ad/main.html', context)



