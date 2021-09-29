from django.forms import widgets
from django.forms.models import ModelFormMetaclass
from . models import Transport_Ad
from ad.forms import CreateForm, TextInput, NumberInput

class TransportForm(CreateForm):
    class Meta(CreateForm.Meta):
        model = Transport_Ad
        fields = CreateForm.Meta.fields + ['brand', 'model', 'year']
        extend_widgets = {
            'brand': TextInput(attrs={'class': 'form-control',  'aria-describedby': 'brand_input'}),
            'model': TextInput(attrs={'class': 'form-control',  'aria-describedby': 'model_input'}),
            'year': NumberInput(attrs={'class': 'form-control', 'aria-describedby': 'year_input'}),
        }
        widgets = {**CreateForm.Meta.widgets, **extend_widgets}
