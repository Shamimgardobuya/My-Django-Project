from django import forms
from . import models

class PatientRegisterationForm(forms.ModelForm):
    class Meta:
        model=models.Patient  #link with the model that you want a form with 
        fields=['firstname','lastname','date_of_birth','gender','age','phone_number','date_of_registeration','registrar']   #use all fields of class patient 
# class VitalsRegisterationForm(forms.ModelForm):
#     class Meta:
#         model=models.Vitals
#         fields='__all__'
# class VisitRegisteration(forms.ModelForm):
#     class Meta:
#         model=models.Vitals
#         fields='__all__'