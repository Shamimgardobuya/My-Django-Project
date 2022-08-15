from cProfile import label
from django import forms
from . import models

class PatientRegistrationForm(forms.ModelForm):
    class Meta:
        model=models.Patient  #link with the model that you want a form with 
        fields=['firstname','lastname','date_of_birth','gender','age','phone_number','date_of_registeration','registrar']   #use all fields of class patient 
        labels={
            'firstname':'First Name',
            'lastname':'Last Name',
            'date_of_birth':'Date of birth',
            'gender':'Gender',
            'age':'Age',
             'phone_number':'Phone Number',
             'date_of_registeration':"Registeration date",
             'registrar':'Registerar'
        }
        widgets={
           "firstname": forms.PasswordInput(attrs={ 'class': "form-control",'type':'firstname', "placeholder":"Enter your firstname"}),
           "lastname": forms.PasswordInput(attrs={ 'class': "form-control",'type':'laststname', "placeholder":"Enter your lastname"}),
           "date_of_birth": forms.PasswordInput(attrs={ 'class': "form-control",'type':'date_of_birth', "placeholder":"date of birth"}),
            # 'gender': forms.PasswordInput(attrs={ 'type':'gender', "placeholder":"Your Gender"}),
            'age': forms.PasswordInput(attrs={ 'class': "form-control",'type':'age', "placeholder":"Your Age"}),
             'phone_number':forms.PasswordInput(attrs={ 'class': "form-control",'type':'phone_number', "placeholder":"Please enter your phone number"}),
            # 'date_of_registeration':forms.PasswordInput(attrs={ 'type':'Registeration date', "placeholder":"Date of registeration"}),
            'registrar':forms.PasswordInput(attrs={ 'class': "form-control",'type':'register', "placeholder":"Your registrar"}),
        }

        
class VitalsRegistrationForm(forms.ModelForm):
    class Meta:
        model=models.Vitals
        fields=['patient_name','visit_date','height','weight']
class VisitRegistration(forms.ModelForm):
    class Meta:
        model=models.PatientVisit
        fields='__all__'