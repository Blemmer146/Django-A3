from django.shortcuts import render
from django.conf import settings
import django
import sys

def debug(request):
    """
    Simple debug view with basic project information
    """
    context = {
        'project_name': 'SessionManagement',
        'app_name': 'Manager',
        'django_version': django.get_version(),
        'python_version': f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        'debug_status': settings.DEBUG,
    }

    return render(request, 'testapp/index.html', context)

def session_count(request):
    print('Total cookies:', request.COOKIES)
    """
    View to count the number of active sessions
    """
    count=int(request.COOKIES.get('count', 0))
    count+=1
    response = render(request, 'testapp/session_count.html', {'count': count})
    response.set_cookie('count',count)
    return response