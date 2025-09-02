from django.shortcuts import render
from django.conf import settings
import django
import sys
from .models import Detail
from .forms import DetailForm

def debug(request):
    """
    Simple debug view with basic project information
    """
    context = {
        'project_name': 'TempFilter',
        'app_name': 'FilterApp',
        'django_version': django.get_version(),
        'python_version': f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        'debug_status': settings.DEBUG,
    }

    return render(request, 'testapp/index.html', context)

def form(request):
    if request.method == 'POST':
        form = DetailForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    else:
        form = DetailForm()  # Empty Form
    return render(request, 'testapp/form.html', {'form': form})


def data(request):
    """
    Render the data page.
    """
    details= Detail.objects.all()
    data = {
        'data': details,
    }

    return render(request, 'testapp/data.html',data)