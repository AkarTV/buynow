from category_other.forms import OtherForm
from category_other.models import Other_Ad
from ad.general_services import show_ad_of_category, show_main_page_of_category, show_ad_creation_page, show_ad_edditing_page

def other(request):
    '''return the page with the list of all other category ads'''
    return show_main_page_of_category(request, Other_Ad, 'category_other/other.html')

def create_other(request):
    '''return the page with "other category" ad form to create new "other" ad'''
    return show_ad_creation_page(request, OtherForm, 'category_other/create_other.html')

def show_other_ad(request, category_other_id):
    '''return the page of the curent ad view by its id'''
    return show_ad_of_category(request, Other_Ad, category_other_id, 'category_other/show_other.html')

def edit_other_ad(request, category_other_id):
    '''return the page for the editting ad by its id'''
    return show_ad_edditing_page(request, Other_Ad, OtherForm, category_other_id, 'category_other/edit_other.html')