from django.contrib import admin
from Demo.models import NishantUser
# Register your models here.
class NishantUserInfo(admin.ModelAdmin):
    list_display = ['username', 'email', 'age']
admin.site.register(NishantUser, NishantUserInfo)
