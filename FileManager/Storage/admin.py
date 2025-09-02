from django.contrib import admin
from Storage.models import UserProfile
# Register your models here.
class UserInfo(admin.ModelAdmin):
    list_display = ['username', 'mob_no', 'email', 'timestamp']
admin.site.register(UserProfile, UserInfo)