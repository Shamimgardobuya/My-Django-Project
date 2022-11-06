from . import views

from django.urls import path
from unicodedata import name


urlpatterns=[
    # path('register_user/',views.register,name='registerUser'),
    path("login/", views.login_request, name="login")
   


    
]
