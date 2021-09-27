from django.shortcuts import render, redirect
from . models import Other_Ad
from . forms import OtherForm

#Other page view
def other(request):
    items = Other_Ad.objects.order_by('-date')
    context = {'ads': items}
    return render(request, 'category_other/other.html', context)


def create_other(request):
    if request.method != 'POST':
        form = OtherForm()
    else:
        form = OtherForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    context = {'form': form}
    return render(request, 'category_other/create_other.html', context)