from django.db.models.base import Model
#from django.forms.widgets import NumberInput
from . models import Other_Ad
from django.forms import ModelForm, TextInput, Textarea, NumberInput

class OtherForm(ModelForm):
    class Meta:
        model = Other_Ad
        fields = ['title', 'text', 'max_price']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок объявления'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание объявления'}),
            'max_price': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите максимальную цену (РУБ)'})
            }