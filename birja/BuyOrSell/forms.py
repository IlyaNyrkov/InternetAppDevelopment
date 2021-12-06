from django.db.models import fields
from django.forms import widgets
from django.forms.models import ModelForm
from .models import CryptoCurrencyInfo
from django.forms import ModelForm, TextInput, Textarea, NumberInput, FileInput

class CryptoCurrencyInfoForm(ModelForm):
    class Meta:
        model = CryptoCurrencyInfo
        fields = ["name", "dollar_price", "euro_price", "rubles_price", "logo", "description"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter crypto currency name'
            }),
            "task": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter crypto currency value in dollars'
            }),
            "task": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter crypto currency value in euros'
            }),
            "task": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter crypto currency value in rubles'
            }),
            "task": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Load CryptoCurrency logo',
                'required' : False
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter crypto currency description'
            })
        }