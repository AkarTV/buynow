from django.http import request
from django.shortcuts import render
from . models import Transport_Ad


#Transport page view
def transport(request):
    items = Transport_Ad.objects.order_by('-date')
    context = {'ads': items}
    return render(request, 'category_transport/transport_list.html', context)
