from django.db.models.base import Model
from . models import *
from django.forms import ModelForm, TextInput, Textarea

class OtherForm(ModelForm):
    class Meta:
        model = Other_Ad
        fields = ['title', 'text', 'max_price']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок объявления'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание объявления'}),
            }