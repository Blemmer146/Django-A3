from django.contrib import admin
from DataFaker.models import FakeUser
# Register your models here.
class Data(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone_number', 'age']
admin.site.register(FakeUser,Data)