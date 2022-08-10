# from pyexpat import models
from django.shortcuts import render
from django  import forms
from datetime import date, datetime
from phonenumber_field .modelfields import PhoneNumberField
from django.db import models


# Create your views here.
class Patient(models.Model):
    firstname=models.CharField(max_length=34)
    lastname=models.CharField(max_length=34)
    date_of_birth=models.DateField()
    patient_number=models.IntegerField()
    gender=(
        ('M','Male'),
        ('F','Female')
    )
    gender=models.CharField(choices=gender,max_length=6,null=True)
    age=models.SmallIntegerField()
    phone_number=PhoneNumberField(null=True)
    date_of_registeration=models.DateField()
    registrar=models.CharField(max_length=29)


class Vitals(models.Model):
    patient_name=models.ForeignKey(Patient,on_delete=models.PROTECT,null=True)
    visit_date=models.DateTimeField(default=datetime.now)
    height=models.FloatField()
    weight=models.FloatField()
   
    
class PatientVisit(models.Model):
    patient_name=models.ForeignKey(Patient,on_delete=models.CASCADE,null=True)
    visit_Date=models.DateTimeField(default=datetime.now)
    gen_health=(
        ('g','Good'),
        ('p','Poor')
    )
    general_health=models.CharField(choices=gen_health,null=True,max_length=4)
    choicing=(
        ('y','Yes'),
        ('n','No')
    ) 
    Have_you_ever_been_on_diet=models.CharField(max_length=15,null=True,choices=choicing)
    comments=models.TextField()
    

