from django.contrib import admin
from .models import Detail
# Register your models here.

class DetailAdmin(admin.ModelAdmin):
    """
    Admin interface for the Detail model.
    """
    list_display = ['id','name', 'age', 'email']
admin.site.register(Detail, DetailAdmin)

