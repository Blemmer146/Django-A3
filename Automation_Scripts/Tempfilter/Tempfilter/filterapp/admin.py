
from django.contrib import admin
from filterapp.models import StuModel
# Register your models here.
class Admin_Std(admin.ModelAdmin):
    list_display = ['id','name','age','email']
admin.site.register(StuModel, Admin_Std)