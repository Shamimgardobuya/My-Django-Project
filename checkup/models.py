# from pyexpat import models
from django.shortcuts import render
from django  import forms
from datetime import date, datetime
from phonenumber_field .modelfields import PhoneNumberField
from django.db import models


# Create your views here.
class Patient(models.Model):
    patient_number=models.BigAutoField(primary_key=True)
    firstname=models.CharField(max_length=34)
    lastname=models.CharField(max_length=34)
    date_of_birth=models.DateField()
    gender2=(
        ('Male','Male'),
        ('Female','Female')
    )
    gender=models.CharField(choices=gender2,max_length=6,null=True)
    age=models.SmallIntegerField()
    phone_number=PhoneNumberField(null=True)
    date_of_registeration=models.DateField()
    registrar=models.CharField(max_length=29)

    def __str__(self):
        return self.firstname


class Vitals(models.Model):
    patient_name=models.ForeignKey(Patient,on_delete=models.PROTECT,null=True)
    visit_date=models.DateTimeField(default=datetime.now)
    height=models.FloatField()
    weight=models.FloatField()    

    def __str__(self):
        return self.patient_name
    
  
     
        

class PatientVisit(models.Model):
    patient_name=models.ForeignKey(Patient,on_delete=models.CASCADE,null=True)
    visit_Date=models.DateTimeField(default=datetime.now)
    gen_health=(
        ('Good','Good'),
        ('Poor','Poor')
    )
    general_health=models.CharField(choices=gen_health,null=True,max_length=4)
    choicing=(
        ('yes','Yes'),
        ('No','No')
    ) 
    Have_you_ever_been_on_diet=models.CharField(max_length=15,null=True,choices=choicing)
    comments=models.TextField()
    
    def __str__(self):
        return str(self.patient_name)

