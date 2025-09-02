from django.shortcuts import render
import datetime
# Create your views here.
def Show(request):
    dt = datetime.datetime.now()
    dic = {'date': dt}
    return render(request, 'testapp/index1.html',dic)