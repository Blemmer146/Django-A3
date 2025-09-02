from django import forms

class Registration(forms.Form):
    name=forms.CharField(max_length=20)
    roll=forms.IntegerField()
    marks=forms.IntegerField()