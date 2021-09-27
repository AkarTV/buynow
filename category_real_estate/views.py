from django.shortcuts import render
from . models import Real_Estate_Ad

#Real estate page view
def real_estate(request):
    items = Real_Estate_Ad.objects.order_by('-date')
    context = {'ads': items}
    return render(request, 'category_real_estate/real_estate.html', context)
