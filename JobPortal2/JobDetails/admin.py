from django.contrib import admin
from JobDetails.models import PuneJob
from JobDetails.models import HyderabadJob
from JobDetails.models import MumbaiJob
# Register your models here.
class Information(admin.ModelAdmin):
    list_display = ['company_name', 'designation', 'package', 'location', 'email', 'contact_number']
admin.site.register(PuneJob, Information)
admin.site.register(HyderabadJob, Information)
admin.site.register(MumbaiJob, Information)