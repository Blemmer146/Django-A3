from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name='Student Name')
    age = models.PositiveIntegerField(verbose_name='Age')
    email = models.EmailField(verbose_name='Email Address')
