from django.shortcuts import render
from Demo.models import NishantUser
# Create your views here.
def show(request):
    data=NishantUser.objects.all()
    dic={
        'name': 'Nishant',
         'data': data
    }

    return render(request, 'testapp/index.html', dic)

def home(request):
    dic = {'list': ['Nishant', 'Shivam', 'Saurabh', 'Ankit']}

    return render(request, 'testapp/home.html', dic)
