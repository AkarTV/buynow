from . models import Real_Estate_Ad
from . forms import RealEstateForm
from django.shortcuts import redirect

def get_real_estate_ads_dict():
    '''return "real estate category" ads from DB in dict sorted by date'''
    items = Real_Estate_Ad.objects.order_by('-date')
    return {'ads': items}

def get_real_estate_ad_form(request):
    '''return category real estate form'''
    if request.method != 'POST':
        form = RealEstateForm()
    else:
        form = RealEstateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    return {'form': form}

def get_real_estate_ad_from_DB(ad_id):
    '''return the "real estate category" ad in dict by the id'''
    ad = Real_Estate_Ad.objects.get(id=ad_id)
    return {'ad' : ad}