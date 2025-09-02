from django.shortcuts import render
from django.conf import settings
import django
import sys
from .forms import LoginForm
import datetime as dt
def debug(request):
    """
    Simple debug view with basic project information
    """
    context = {
        'project_name': 'DemoWebsite',
        'app_name': 'LoginForm',
        'django_version': django.get_version(),
        'python_version': f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        'debug_status': settings.DEBUG,
    }

    return render(request, 'testapp/index.html', context)

def homepage(request):
    """
    Render the homepage of the application.
    """
    form=LoginForm()
    return render(request, 'testapp/homepage.html', {'form': form})

def second_view(request):
    """
    Render a second view for demonstration purposes.
    """
    name=request.GET['name']
    response= render(request, 'testapp/second_view.html', {'name':name})
    response.set_cookie('name', name)
    return response

def final_view(request):
    """
    Render the final view, retrieving the name from cookies.
    """
    name = request.COOKIES.get('name')
    time= dt.datetime.now().strftime( "%Y-%m-%d %H:%M:%S")
    return render(request, 'testapp/final_view.html', {'name': name, 'time': time})