from django.shortcuts import render, redirect
from . models import Transport_Ad
from . forms import TransportForm


#Transport page view
def transport(request):
    items = Transport_Ad.objects.order_by('-date')
    context = {'ads': items}
    return render(request, 'category_transport/transport_list.html', context)

def create_transport(request):
    if request.method != 'POST':
        form = TransportForm()
    else:
        form = TransportForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    context = {'form': form}
    return render(request, 'category_transport/create_transport.html', context)