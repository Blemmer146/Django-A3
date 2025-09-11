from django.shortcuts import render
from django.conf import settings
import django
import sys
from .forms import EmployeeForm
from .models import Employee

def debug(request):
    """
    Simple debug view with basic project information
    """
    context = {
        'project_name': 'EmpManage',
        'app_name': 'EmpDetail',
        'django_version': django.get_version(),
        'python_version': f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        'debug_status': settings.DEBUG,
    }

    return render(request, 'testapp/index.html', context)

def empdetails(request):
    data = Employee.objects.all()
    return render(request, 'testapp/empdetails.html', {'data': data})