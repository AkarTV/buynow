from .models import Real_Estate_Ad
from .forms import RealEstateForm
from ad.general_services import show_main_page_of_category, show_ad_of_category, show_ad_creation_page, show_ad_edditing_page

def real_estate(request):
    '''return the page with the list of all real estate category ads'''
    return show_main_page_of_category(request, Real_Estate_Ad, 'category_real_estate/real_estate.html')

def create_real_estate(request):
    '''return the page with "real estate category" ad form to create new "real estate" ad'''
    return show_ad_creation_page(request, RealEstateForm, 'category_real_estate/create_real_estate.html')

def show_real_estate_ad(request, real_estate_id):
    '''return the page of the curent ad by its id'''
    return show_ad_of_category(request, Real_Estate_Ad, real_estate_id, 'category_real_estate/show_real_estate_ad.html')

def edit_real_estate_ad(request, real_estate_id):
    return show_ad_edditing_page(request, Real_Estate_Ad, RealEstateForm, real_estate_id, 'category_real_estate/edit_real_estate.html')