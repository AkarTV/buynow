from django.http import request
from django.shortcuts import render, redirect
from category_transport.models import Transport_Ad
from category_real_estate.models import Real_Estate_Ad
from category_other.models import Other_Ad
from itertools import chain
from operator import attrgetter
from category_transport.views import show_transport_ad
from category_real_estate.views import show_real_estate_ad
from category_other.views import show_other_ad

#Main page
def main(request):      
    transport = Transport_Ad.objects.all()
    houses = Real_Estate_Ad.objects.all()
    other = Other_Ad.objects.all() 
    result = sorted(chain(transport, houses, other), key=attrgetter('date'), reverse=True)
    context = {'ads': result}
    return render(request, 'ad/main.html', context)

def choose_category(request):
    return render(request, 'ad/choose_category.html')

def show_ad(request, category: str, ad_id):
    if category == 'Транспорт':
        return show_transport_ad(request, ad_id)
    elif category == 'Недвижимость':
        return show_real_estate_ad(request, ad_id)
    elif category == 'Другое':
        return show_other_ad(request, ad_id)




