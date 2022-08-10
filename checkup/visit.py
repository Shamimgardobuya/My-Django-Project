
from . import models
from django import forms

class VisitRegistration(forms.ModelForm):
    class Meta:
        model=models.PatientVisit
        fields='__all__'