import datetime

from django.shortcuts import render
# Create your views here.
def Show(request):
    dt=datetime.datetime.now()
    dic={'date':dt}
    return render(request,'testapp/index2.html',dic)