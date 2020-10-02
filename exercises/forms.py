from django.forms import ModelForm, DateInput, TextInput
from exercises.models import Bank
import datetime

from django import forms
from django.utils.dateparse import parse_duration




class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = [
            'day',
            'duration',
            'place',
            'place_description',
            'description',
            'photo',
            'film',
            'rating']
        widgets = {
            'day': DateInput(format='%d/%m/%Y', attrs={'placeholder': 'dd/mm/yyyy'}),

        }
       