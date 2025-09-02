from django.shortcuts import render
from django.conf import settings
import django
import sys
from .forms import StudentForm

def debug(request):
    """
    Simple debug view with basic project information
    """
    context = {
        'project_name': 'SchoolDetails',
        'app_name': 'StudentForms',
        'django_version': django.get_version(),
        'python_version': f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        'debug_status': settings.DEBUG,
    }

    return render(request, 'testapp/index.html', context)

def StudentOperation(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    else:
        form= StudentForm() #Empty Form
    return render( request, 'testapp/studform.html', {'form': form})