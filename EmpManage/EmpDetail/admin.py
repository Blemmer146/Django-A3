from django.contrib import admin
from .models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'role', 'designation', 'salary']
admin.site.register(Employee, EmployeeAdmin)