from django.shortcuts import render
from django.conf import settings
import django
import sys

from FormApp2.forms import Registration


def debug(request):
    """
    Simple debug view with basic project information
    """
    context = {
        'project_name': 'DjangoForms2',
        'app_name': 'FormApp2',
        'django_version': django.get_version(),
        'python_version': f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        'debug_status': settings.DEBUG,
    }

    return render(request, 'testapp/index.html', context)

def forms(request):
    """
    View to render the form page
    """
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            print('Thanks for submitting the form')
            print(f'''
            Here is your submitted data
                  {form.cleaned_data['name']}
                  {form.cleaned_data['age']}
                  {form.cleaned_data['email']}
                  {form.cleaned_data['feedback']}
                  ''')
    else:
        form = Registration()
    return render(request, 'testapp/feedback.html', {'form': form})