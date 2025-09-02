from django.contrib import admin
from .models import Movie
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = [ 'id','movie_name', 'release_date', 'main_hero', 'main_heroine', 'language', 'rating']
admin.site.register(Movie, MovieAdmin)