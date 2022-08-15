from dataclasses import field
from http.client import HTTPResponse
from django.shortcuts import render,redirect

from .models import Vitals

# from checkup import visit, vitals
from . import forms


def home_page(request):
    return render(request,'checkup/index.html')

def registering_patient(request):
    if request.method=='POST':

      form=forms.PatientRegistrationForm(request.POST)  #name of file #creating an acceptance of the whole form
      if form .is_valid():
        form.save()
        # data = ['Your registration is completed successfully.<br />', 'Name:', field, '<br />', 'Email:', field, '<br />', 'Username:', field]
      return redirect('home_page')

    else:
           form=forms.PatientRegistrationForm()
           return render(request,'checkup/registerpatient.html',{
        "register":form
           })

def registerVitals(request):
  shamim=Vitals.objects.all()
  if request.method=='POST':
    vital=forms.VitalsRegistrationForm(request.POST)
    if vital.is_valid():
        vital.save()
    return redirect('vital_checkup')

  else:
    vital=forms.VitalsRegistrationForm()   #only when blank
    return render(request,'checkup/vitals.html',{
      "your_vitals":vital,'shamim':shamim
    })
  

def visit_register(request):
  if request.method=='POST':
    visit_1=forms.VisitRegistration(request.POST)  #Name of file 
    if visit_1.is_valid():
      visit_1.save()
    return redirect('home_page')
  else:
    visit_1=forms.VisitRegistration()
    return render(request,'checkup/visitform.html',{
      'visit_me':visit_1      #storing the object
    })

# def calculating_bmi(height,weight):
#       z=height*height
#       w=weight/z
#       print(w)

# def my_values(request):
#   value=Vitals.height
#   return render(request,'checkup/calculate.html',{
#     "values":value
#   })
 
     