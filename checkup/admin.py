from django.contrib import admin
from . import models
# from . import Vitals
# Register your models here.
admin.site.register(models.Patient)
admin.site.register(models.Vitals)
admin.site.register(models.PatientVisit)
# admin.site.register(models.Vitals)
# admin.site.register(models.Vitals)
# class VitalsAdmin(admin.ModelAdmin):
#      list_display=('id','bmi')
#      search_fields=()
# admin.site.register(models.Vitals,VitalsAdmin)
