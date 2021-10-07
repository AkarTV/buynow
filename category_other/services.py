from . models import Other_Ad
from . forms import OtherForm
from django.shortcuts import redirect

def get_other_ads_dict():
    '''return "other category" ads from DB in dict sorted by date'''
    items = Other_Ad.objects.order_by('-date')
    return {'ads': items}

def get_other_ad_form(request):
    '''return category other form'''
    if request.method != 'POST':
        form = OtherForm()
    else:
        form = OtherForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    return {'form': form}

def get_other_ad_from_DB(ad_id):
    '''return the "other category" ad in dict by the id'''
    ad = Other_Ad.objects.get(id=ad_id)
    return {'other_ad' : ad}