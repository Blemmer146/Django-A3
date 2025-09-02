from django.shortcuts import render
from django.conf import settings
import django
import sys
from JobDetails.models import PuneJob
from JobDetails.models import HyderabadJob
from JobDetails.models import MumbaiJob

def debug(request):
    """
    Simple debug view with basic project information
    """
    context = {
        'project_name': 'JobPortal2',
        'app_name': 'JobDetails',
        'django_version': django.get_version(),
        'python_version': f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        'debug_status': settings.DEBUG,
    }

    return render(request, 'testapp/index.html', context)

def home(request):
    """
    Home view that renders the home page
    """
    return render(request, 'testapp/mainpage.html')

def pune(request):
    """
    View for Pune jobs
    """
    dic= {
        'city': 'Pune',
        'jobs': PuneJob.objects.all()  # Fetch all Pune jobs from the database
          }
    return render(request, 'testapp/jobs.html',dic)

def hyd(request):
    """
    View for Hyderabad jobs
    """
    dic= {
        'city': 'Hyderabad',
        'jobs': HyderabadJob.objects.all()  # Fetch all Hyderabad jobs from the database
          }
    return render(request, 'testapp/jobs.html',dic)

def mum(request):
    """
    View for Mumbai jobs
    """
    dic= {
        'city': 'Mumbai',
        'jobs': MumbaiJob.objects.all()  # Fetch all Mumbai jobs from the database
          }
    return render(request, 'testapp/jobs.html',dic)