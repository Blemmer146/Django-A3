from django import forms
from MovieApp.models import Movie
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'