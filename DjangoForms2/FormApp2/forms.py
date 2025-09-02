from django import forms
from django.core import validators
import re

def chklen(value):
    print('Checking length')
    if len(value) < 4:
        raise forms.ValidationError('Length should be greater than 4 characters')

def chkage(value):
    print('Checking age')
    if value < 18:
        raise forms.ValidationError('Age should be greater than or equal to 18')
    elif value > 100:
        raise forms.ValidationError('Age should be less than or equal to 100')

def chkemail(value):
    print('Checking email')
    if not re.match(r'^[a-zA-Z0-9._%+-]+@(?:gmail|yahoo|rediff|outlook|hotmail)\.com$', value):
        raise forms.ValidationError('Invalid email format')

class Registration(forms.Form):
    name=forms.CharField(max_length=20, validators=[chklen])
    age=forms.IntegerField(validators=[chkage])
    email=forms.EmailField(validators=[chkemail])
    feedback=forms.CharField(widget=forms.Textarea, required=False)