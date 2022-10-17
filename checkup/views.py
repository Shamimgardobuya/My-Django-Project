from django.http import JsonResponse
from django.core import serializers
from dataclasses import field
from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.views.generic.base import View
from checkup.models import Patient
from django.shortcuts import render,redirect
from Users.user_registration import NewUserForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm 

from django.contrib import messages



from .models import Patient,PatientVisit,Vitals

# from checkup import visit, vitals
from . import forms

def patient_dashboard(request):
    return render(request,"checkup/dashboard_.html",{})

def pivot_data(request):
    dataset = PatientVisit.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)

def visit(request):
  all_visits=PatientVisit.objects.all()
  return render (request,"checkup/all_visits.html",{"visits":all_visits})

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
      print(form.errors)
      return render (request,'checkup/registerpatient.html',{"register":form
    })


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


@property
def calc_bmi(self):
        into_meter=100/self.height
        bmi=(into_meter^2)/self.weight
        # bmi=44
        return bmi
    

# def calculating_bmi(height,weight):
#       z=height*height
#       w=weight/z
#       print(w)

# def my_values(request):
#   value=Vitals.height
#   return render(request,'checkup/calculate.html',{
#     "values":value
#   })

def all_patients(request):
  patients_all=Patient.objects.all()
  return render(request,'checkup/viewall.html',{
    'allpatients':patients_all
  })
 


def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user=form.save()
			login(request,user)
			# messages.success(request, "Registration successful." )
			return redirect("home_page")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	
	form = NewUserForm()
	return render (request=request, template_name="Users/register_user.html", context={"form":form})

# def loging_in(request):
#     if request.method=="POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#           login(request, user)
#         else:
#          messages.success(("There was an error loging you in,Try again"))
#          return redirect('home')
#     else:
#         return render(request,"Users/loging_in.html",{
            
            
#         })
        
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home_page")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="Users/loging_in.html", context={"login_form":form})

# @login()
# def profile(request):
#     return render (request,"Users/profile.html",{"users":user})


