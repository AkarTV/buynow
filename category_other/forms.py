from django.forms import widgets
from django.forms.models import ModelFormMetaclass
from . models import Other_Ad
from ad.forms import CreateForm

class OtherForm(CreateForm):
    '''Category other ad form'''
    class Meta(CreateForm.Meta):
        model = Other_Ad
