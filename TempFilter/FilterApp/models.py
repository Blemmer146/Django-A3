from django.db import models

# Create your models here.

class Detail(models.Model):
    """
    Model to store details of the filter application.
    """
    name = models.CharField(max_length=100)
    age= models.IntegerField()
    email = models.EmailField()
