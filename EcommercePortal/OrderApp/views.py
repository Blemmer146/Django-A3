from django.shortcuts import render, redirect
from django.conf import settings
import django
import sys
from .forms import OrderForm

def debug(request):
    """
    Simple debug view with basic project information
    """
    context = {
        'project_name': 'EcommercePortal',
        'app_name': 'OrderApp',
        'django_version': django.get_version(),
        'python_version': f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        'debug_status': settings.DEBUG,
    }

    return render(request, 'testapp/index.html', context)

def home(request):
    return render(request, 'testapp/home.html')

def form(request):
    render(request, 'testapp/form.html')

def data(request):
    item = request.COOKIES.get('item')
    quantity = request.COOKIES.get('quantity')

    return render(request, 'testapp/data.html', {'item': item,'quantity': quantity})

