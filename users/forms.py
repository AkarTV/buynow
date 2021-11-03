from django.db.models import fields
from django.forms import ModelForm, widgets, EmailField, TextInput
from django.contrib.auth.models import User
from .models import Customer

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', ]

class CustomerForm(ModelForm):
    class Meta:
        model =Customer
        fields = ['phone_number', 'avatar']