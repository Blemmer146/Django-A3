from django.shortcuts import render
from Storage.models import UserProfile
# Create your views here.
def db(request):
    data=UserProfile.objects.all()
    dic={
        'data': data
    }
    return render(request, 'testapp/index.html',dic)