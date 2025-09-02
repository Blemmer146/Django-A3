from django.shortcuts import render
from django.conf import settings
import django
import sys
from .forms import MovieForm
from .models import Movie
def debug(request):
    """
    Simple debug view with basic project information
    """
    context = {
        'project_name': 'MoviePortal',
        'app_name': 'MovieApp',
        'django_version': django.get_version(),
        'python_version': f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        'debug_status': settings.DEBUG,
    }

    return render(request, 'testapp/index.html', context)

def moviehome(request):
    """
    Home view for the MovieApp
    """
    return render(request, 'testapp/moviehome.html')

def movielist(request):
    """
    List view for displaying all movies
    """
      # Importing here to avoid circular import issues
    movies = Movie.objects.all()
    dic={
        'movies': movies
    }
    return render(request, 'testapp/movielist.html', dic )

def movieform(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    else:
        form = MovieForm()  # Empty Form
    return render(request, 'testapp/movieform.html', {'form': form})