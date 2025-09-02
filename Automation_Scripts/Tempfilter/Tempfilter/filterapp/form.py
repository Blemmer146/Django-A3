from django import forms
from filterapp.models import StuModel


class Student_Regis(forms.ModelForm):
    name=forms.CharField()
    age=forms.CharField()
    email=forms.EmailField()
    class Meta:
        model=StuModel
        fields='__all__'