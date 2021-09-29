from django.shortcuts import render, redirect
from . models import Real_Estate_Ad
from .forms import RealEstateForm

#Real estate page view
def real_estate(request):
    items = Real_Estate_Ad.objects.order_by('-date')
    context = {'ads': items}
    return render(request, 'category_real_estate/real_estate.html', context)

def create_real_estate(request):
    if request.method != 'POST':
        form = RealEstateForm()
    else:
        form = RealEstateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    context = {'form': form}
    return render(request, 'category_real_estate/create_real_estate.html', context)