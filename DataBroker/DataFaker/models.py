from django.db import models

# Create your models here.
class FakeUser(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    age = models.IntegerField(null=True, blank=True)
