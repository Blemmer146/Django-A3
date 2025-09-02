from django.db import models

# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=150, unique=True)
    mob_no = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    timestamp = models.DateTimeField(auto_now_add=True)
