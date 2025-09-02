from django import forms
from StudentForms.models import Student
class StudentForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='Student Name')
    age = forms.IntegerField(min_value=1, label='Age')
    email = forms.EmailField(label='Email Address')

    class Meta:
        model = Student
        fields='__all__'

