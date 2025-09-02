from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
import django
import sys

def debug(request):
    """
    Simple debug view with basic project information
    """
    context = {
        'project_name': 'Authentication',
        'app_name': 'AuthApp',
        'django_version': django.get_version(),
        'python_version': f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        'debug_status': settings.DEBUG,
    }

    return render(request, 'testapp/index.html', context)

def auth(request):
    return render(request,'testapp/base.html')
def home(request):
    return render(request,'testapp/home.html')

@login_required
def pythonexam(request):

    return render(request,'testapp/pythonexam.html')

@login_required
def javaexam(request):

    return render(request,'testapp/javaexam.html')

@login_required
def sqlexam(request):

    return render(request,'testapp/sqlexam.html')

@login_required
def aptiexam(request):

    return render(request,'testapp/aptiexam.html')

def logout(request):
    return render(request,'testapp/logout.html')

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'testapp/signup.html', {'form': form})