from django.http import request
from django.shortcuts import render
from .services import get_all_ads, show_ad

def main(request):
    '''return the main page with all ads'''
    context = get_all_ads()
    return render(request, 'ad/main.html', context)

def show_ad_from_main(request, category, ad_id):
    '''return the ad page from main page'''
    return show_ad(request, category, ad_id)

def choose_category(request):
    '''return the page to select a category to add new ad'''
    return render(request, 'ad/choose_category.html')

