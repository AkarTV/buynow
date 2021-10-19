from .models import Transport_Ad
from .forms import TransportForm
from ad.general_services import show_main_page_of_category, show_ad_of_category, show_ad_creation_page, show_ad_edditing_page

def transport(request):
    '''return the page with the list of all transport category ads'''
    return show_main_page_of_category(request, Transport_Ad, 'category_transport/transport_list.html')

def create_transport(request):
    '''return the page with "transport category" ad form to create new "transport" ad'''
    return show_ad_creation_page(request, TransportForm, 'category_transport/create_transport.html')

def show_transport_ad(request, transport_id):
    '''return the page of the curent ad by its id'''
    return show_ad_of_category(request, Transport_Ad, transport_id, 'category_transport/show_transport_ad.html')

def edit_transport_ad(request, transport_id):
    return show_ad_edditing_page(request, Transport_Ad, TransportForm, transport_id, 'category_transport/edit_transport.html')