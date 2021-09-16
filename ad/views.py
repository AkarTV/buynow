from django.http import request
from django.shortcuts import render, redirect
from . models import *
from itertools import chain
from operator import attrgetter
from . forms import OtherForm

#Main page
def main(request):  
    transport = Transport_Ad.objects.all()
    houses = Real_Estate_Ad.objects.all()
    other = Other_Ad.objects.all() 
    result = sorted(chain(transport, houses, other), key=attrgetter('date'), reverse=True)
    context = {'ads': result}
    return render(request, 'ad/main.html', context)

#Function for viewing ads page of category
def show_ad_of_category(Category_Ad_Model, template, request):
    items = Category_Ad_Model.objects.order_by('-date')
    context = {'ads': items}
    return render(request, template, context)

#Transport page view
def transport(request):
    show_ad_of_category(Transport_Ad, 'ad/transport.html', request)

#Real estate page view
def real_estate(request):
    show_ad_of_category(Real_Estate_Ad, 'ad/real_estate.html', request)

#Other page view
def other(request):
    show_ad_of_category(Other_Ad, 'ad/other.html', request)

#
def create_other(request):
    if request.method != 'POST':
        form = OtherForm()
    else:
        form = OtherForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    context = {'form': form}
    return render(request, 'ad/create_other.html', context)
