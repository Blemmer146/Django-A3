from django import forms
from django.core import validators
import re



class Registration(forms.Form):
    name=forms.CharField(max_length=20)
    age=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea, required=False)

    def clean(self):
        cleaned_data = super().clean()
        name_data= cleaned_data["name"]
        if name_data[0].upper()!='S':
            raise forms.ValidationError("Name should start with 'S'")

        email_data = cleaned_data["email"]
        if email_data[-10]!='@gmail.com':
            raise forms.ValidationError("Email should end with '@gmail.com'")

