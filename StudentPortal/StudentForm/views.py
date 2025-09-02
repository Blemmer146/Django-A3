from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import datetime
# Create your views here.
def Show(request):
    dic= {
    'name':'Vibhor',
    'age': 20,
    'salary': 100000,
    }
    return render(request, 'testapp/indexstp.html',dic)