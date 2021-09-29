from django.forms import widgets
from django.forms.models import ModelFormMetaclass
from . models import Other_Ad
from ad.forms import CreateForm

class OtherForm(CreateForm):
    class Meta(CreateForm.Meta):
        model = Other_Ad
