from django import forms
from . import models

class PatientRegistrationForm(forms.ModelForm):
    class Meta:
        model=models.Patient  #link with the model that you want a form with 
        # fields=('firstname','lastname','date_of_birth','gender','age','phone_number','date_of_registeration','registrar')   #use all fields of class patient,a tuple 
        fields='__all__'
        # labels={
        #     'firstname':'First Name',
        #     'lastname':'Last Name',
        #     'date_of_birth':'Date of birth',
        #     'gender':'Gender',
        #     'age':'Age',
        #      'phone_number':'Phone Number',
        #      'date_of_registeration':"Registeration date",
        #      'registrar':'Registerar'
        # }
        widgets={
           "firstname": forms.TextInput(attrs={ 'class': "form-control"}),
           "lastname": forms.TextInput(attrs={ 'class': "form-control"}),
           "date_of_birth": forms.TextInput(attrs={ 'class': "form-control"}),
            'gender': forms.Select(attrs={ 'type':'gender', 'class': "form-control"}),
            'age': forms.NumberInput(attrs={ 'class': "form-control"}),
            'phone_number':forms.NumberInput(attrs={ 'class': "form-control"}),
            'date_of_registeration':forms.TextInput(attrs={  'class': "form-control",'type':'Registeration date', "placeholder":"Date of registeration"}),
            'registrar':forms.TextInput(attrs={ 'class': "form-control"}),
        }
        # def __init__(self,*args,**kwargs):
            # super().__init__(*args,**kwargs)
        

        
class VitalsRegistrationForm(forms.ModelForm):
    class Meta:
        model=models.Vitals
        fields=['patient_name','visit_date','height','weight']
        widgets={
           "patient_name": forms.TextInput(attrs={ 'class': "form-control"}),
        #    "lastna: forms.TextInput(attrs={ 'class': "form-control"}),
           "visit_date": forms.TextInput(attrs={ 'class': "form-control"}),
            # 'gender': forms.PasswordInput(attrs={ 'type':'gender', "placeholder":"Your Gender"}),
            'height': forms.NumberInput(attrs={ 'class': "form-control"}),
            'weight':forms.NumberInput(attrs={ 'class': "form-control"}),
        }
class VisitRegistration(forms.ModelForm):
    class Meta:
        model=models.PatientVisit
        fields='__all__'
        widgets={
           "patient_name": forms.TextInput(attrs={ 'class': "form-control"}),
           "visit_Date": forms.TextInput(attrs={ 'class': "form-control"}),
          
            "Have_you_ever_been_on_diet":forms.TextInput(attrs={'class':"form-control"}),
            'general_health': forms.Select(attrs={ 'class': "form-control"}),
            'comments':forms.Textarea(attrs={ 'class': "form-control"}),

        }