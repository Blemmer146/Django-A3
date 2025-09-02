from django.shortcuts import render
from django.conf import settings
import django
import sys

from FormApp.forms import Registration


def debug(request):
    """
    Simple debug view with basic project information
    """
    context = {
        'project_name': 'DjangoForms',
        'app_name': 'FormApp',
        'django_version': django.get_version(),
        'python_version': f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        'debug_status': settings.DEBUG,
    }

    return render(request, 'testapp/index.html', context)

def forms(request):
    """
    View to render the form page
    """
    if request.method=='POST':
        form = Registration(request.POST)
        if form.is_valid():
            print('Thanks for submitting the form')
            print(f'''
            Here is your submitted data
                  {form.cleaned_data['name']}
                  {form.cleaned_data['roll']}
                  {form.cleaned_data['marks']}
                  ''')
    form=Registration()
    return render(request, 'testapp/stuform.html',{'form': form})