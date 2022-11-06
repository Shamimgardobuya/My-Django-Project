from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class NewUserForm(UserCreationForm):
    email=forms.EmailField(required=True)
    
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        # widgets={
        #     "username": forms.TextInput(attrs={ 'class': "form-control"}),
        #     "email": forms.TextInput(attrs={ 'class': "form-control"}),
          
        #     "password1":forms.TextInput(attrs={'class':"form-control"}),
        #     'password2':forms.Textarea(attrs={ 'class': "form-control"}),
        # }
    def save(self, commit=True):

            user = super(NewUserForm, self).save(commit=False)
            user.email = self.cleaned_data['email']

            if commit:
                user.save()
            return user
  
# class LoginUserForm():
#     email=forms.EmailField(required=True)


