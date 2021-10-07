from typing import Text
from .models import Real_Estate_Ad
from ad.forms import CreateForm, TextInput, NumberInput

class RealEstateForm(CreateForm):
    '''Category real estate ad form'''
    class Meta(CreateForm.Meta):
        model = Real_Estate_Ad
        fields = CreateForm.Meta.fields + ['square', 'location']
        extend_widgets = {
            'square': NumberInput(attrs={'class': 'form-control',  'aria-describedby': 'square_input'}),
            'location': TextInput(attrs={'class': 'form-control',  'aria-describedby': 'location_input'})
        }
        widgets = {**CreateForm.Meta.widgets, **extend_widgets}