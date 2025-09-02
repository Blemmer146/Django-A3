# Create your models here.
from django.db import models

class StuModel(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.EmailField()
