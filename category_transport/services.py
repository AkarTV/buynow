from . models import Transport_Ad
from . forms import TransportForm
from django.shortcuts import redirect

def get_transport_ads_dict():
    '''return "transport category" ads from DB in dict sorted by date'''
    items = Transport_Ad.objects.order_by('-date')
    return {'ads': items}

def get_transport_ad_form(request):
    '''return category transport form'''
    if request.method != 'POST':
        form = TransportForm()
    else:
        form = TransportForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    return {'form': form}

def get_transport_ad_from_DB(ad_id):
    '''return the "transport category" ad in dict by the id'''
    ad = Transport_Ad.objects.get(id=ad_id)
    return {'ad' : ad}