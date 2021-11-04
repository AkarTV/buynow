from django.http import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .services import get_all_ads

def main(request):
    '''return the main page with all ads'''
    context = get_all_ads()
    return render(request, 'ad/main.html', context)

@login_required
def choose_category(request):
    '''return the page to select a category to add new ad'''
    return render(request, 'ad/choose_category.html')

