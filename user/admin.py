from django.contrib import admin
from .models import Patient,Doctor
# Register your models here.
@ admin.register(Patient,Doctor)
class PatientAdmin(admin.ModelAdmin):
    list_display=['FirstName','LastName','UserName','Email','Password','Address','ProfilePicture']


class DoctorAdmin(admin.ModelAdmin):
    list_display=['FirstName','LastName','UserName','Email','Password','ProfilePicture']
