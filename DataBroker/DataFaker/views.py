from django.shortcuts import render
from django.conf import settings
import django
import sys
from DataFaker.models import FakeUser

def debug(request):
    """
    Simple debug view with basic project information
    """
    context = {
        'project_name': 'DataBroker',
        'app_name': 'DataFaker',
        'django_version': django.get_version(),
        'python_version': f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        'debug_status': settings.DEBUG,
    }

    return render(request, 'testapp/index.html', context)

def db(request):
    data= FakeUser.objects.all()
    dic={
        'data': data
    }
    return render(request, 'testapp/data.html', dic)