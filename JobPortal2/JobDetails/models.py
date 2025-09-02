from django.db import models

# Create your models here.
class PuneJob(models.Model):
    company_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    package = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)

class HyderabadJob(models.Model):
    company_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    package = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)

class MumbaiJob(models.Model):
    company_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    package = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
