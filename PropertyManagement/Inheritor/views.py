from django.shortcuts import render
from django.conf import settings
import django
import sys

def debug(request):
    """
    Simple debug view with basic project information
    """
    context = {
        'project_name': 'PropertyManagement',
        'app_name': 'Inheritor',
        'django_version': django.get_version(),
        'python_version': f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        'debug_status': settings.DEBUG,
    }

    return render(request, 'testapp/index.html', context)

def homepage(request):
    """
    Render the homepage of the Property Management application.
    """
    return render(request, 'testapp/homepage.html')
def aboutus(request):
    """
    Render the about us page of the Property Management application.
    """
    return render(request, 'testapp/aboutus.html')