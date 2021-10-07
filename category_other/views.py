from django.shortcuts import render
from .services import get_other_ads_dict, get_other_ad_form, get_other_ad_from_DB

def other(request):
    '''return the page with the list of all other category ads'''
    context = get_other_ads_dict()
    return render(request, 'category_other/other.html', context)


def create_other(request):
    '''return the page with "other category" ad form to create new "other" ad'''
    context = get_other_ad_form(request)
    return render(request, 'category_other/create_other.html', context)


def show_other_ad(request, category_other_id):
    '''return the page of the curent ad by its id'''
    context = get_other_ad_from_DB(category_other_id)
    return render(request, 'category_other/show_other.html', context)