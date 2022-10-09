from . import views

from django.urls import path
from unicodedata import name


urlpatterns=[
    path('register_user/',views.register,name='user'),
    


    
]
