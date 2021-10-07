from django.forms import ModelForm, TextInput, Textarea, NumberInput

class CreateForm(ModelForm):
    '''Base class for the ad form'''
    class Meta:
        fields = ['title', 'text', 'max_price']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control',  'aria-describedby': 'title_input'}),
            'text': Textarea(attrs={'class': 'form-control', 'id': 'text'}),
            'max_price': NumberInput(attrs={'class': 'form-control', 'id': 'max_price', 'aria-describedby': 'priceHelpLine'})
            }