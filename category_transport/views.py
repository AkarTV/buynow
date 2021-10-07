from django.shortcuts import render
from .services import get_transport_ads_dict, get_transport_ad_form, get_transport_ad_from_DB

def transport(request):
    '''return the page with the list of all transport category ads'''
    context = get_transport_ads_dict()
    return render(request, 'category_transport/transport_list.html', context)

def create_transport(request):
    '''return the page with "transport category" ad form to create new "transport" ad'''
    context = get_transport_ad_form(request)
    return render(request, 'category_transport/create_transport.html', context)

def show_transport_ad(request, transport_id):
    '''return the page of the curent ad by its id'''
    context = get_transport_ad_from_DB(transport_id)
    return render(request, 'category_transport/show_transport_ad.html', context)