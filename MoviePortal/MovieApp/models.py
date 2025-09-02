from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_name = models.CharField(max_length=100, verbose_name='Movie Name')
    release_date = models.DateField(verbose_name='Release Date')
    main_hero = models.CharField(max_length=100, verbose_name='Main Hero')
    main_heroine = models.CharField(max_length=100, verbose_name='Main Heroine')
    language = models.CharField(max_length=50, verbose_name='Language')
    rating = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Rating')