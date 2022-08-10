
from . import models
from django import forms

class VitalsRegisterationForm(forms.ModelForm):
    class Meta:
        model=models.Vitals
        fields='__all__'