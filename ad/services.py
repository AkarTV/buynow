from django.forms.models import ModelForm
from category_transport.models import Transport_Ad
from category_real_estate.models import Real_Estate_Ad
from category_other.models import Other_Ad
from itertools import chain
from operator import attrgetter
from category_transport.views import show_transport_ad
from category_real_estate.views import show_real_estate_ad
from category_other.views import show_other_ad

def get_all_ads():
    '''return all ads from DB in dict sorted by date'''
    transport = Transport_Ad.objects.all()
    houses = Real_Estate_Ad.objects.all()
    other = Other_Ad.objects.all() 
    result = sorted(chain(transport, houses, other), key=attrgetter('date'), reverse=True)
    return {'ads' : result}


