from django.contrib import admin
from .models import *
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
  list_display=['name','specialization','Experience','image']


class servicesAdmin(admin.ModelAdmin):
  list_display=['sevicename','serviceimage',]

 
class appointmentadmin(admin.ModelAdmin):
  list_display=['Full_Name','doctor','service','date','time']




admin.site.register(servicesmodel,servicesAdmin)
admin.site.register(docotrmodel,DoctorAdmin)
admin.site.register(Appointment,appointmentadmin)


