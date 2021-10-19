from django.shortcuts import render, redirect

def _get_one_ad_from_database_by_id(Model_object, ad_id):
    '''returns the dict with the current ad (takes from database by its id)'''
    ad = Model_object.objects.get(id=ad_id)
    return {'ad': ad}

def show_ad_of_category(request, Model_object, ad_id, template):
    '''view function which returns a page with the current ad'''
    context = _get_one_ad_from_database_by_id(Model_object, ad_id)
    return render(request, template, context)



def _get_all_ads_in_dict_from_database(Model_object):
    '''returns the list of ads from DB in dict sorted by date'''
    items = Model_object.objects.order_by('-date')
    return {'ads': items}

def show_main_page_of_category(request, Model_object, template):
    context = _get_all_ads_in_dict_from_database(Model_object)
    return render(request, template, context)



def _make_ad_creation_form(request, Model_form):
    '''creates and returns a filling form'''
    if request.method != 'POST':
        #create an empty form
        form = Model_form()
    else:
        #POST method: process the entered data
        form = Model_form(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    return {'form': form}

def show_ad_creation_page(request, Model_form, template):
    context = _make_ad_creation_form(request, Model_form)
    return render(request, template, context)


    
def show_ad_edditing_page(request, Model_object, Model_form, ad_id, template):
    '''returns the form of editting of the current ad'''
    current_ad = Model_object.objects.get(id=ad_id)
    if request.method != 'POST':
        #fill the form with data of the curent ad
        form = Model_form(instance=current_ad)
    else:
        #POST method: process the entered data
        form = Model_form(instance=current_ad, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    context = {'ad': current_ad, 'form': form}
    return render(request, template, context)