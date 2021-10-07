from django.shortcuts import render
from . services import get_real_estate_ads_dict, get_real_estate_ad_form, get_real_estate_ad_from_DB

def real_estate(request):
    '''return the page with the list of all real estate category ads'''
    context = get_real_estate_ads_dict()
    return render(request, 'category_real_estate/real_estate.html', context)

def create_real_estate(request):
    '''return the page with "real estate category" ad form to create new "real estate" ad'''
    context = get_real_estate_ad_form(request)
    return render(request, 'category_real_estate/create_real_estate.html', context)

def show_real_estate_ad(request, real_estate_id):
    '''return the page of the curent ad by its id'''
    context = get_real_estate_ad_from_DB(real_estate_id)
    return render(request, 'category_real_estate/show_real_estate_ad.html', context)