from unicodedata import name
from django.urls import path
# from .views import home_page
from . import views
# from .views import *

urlpatterns=[
    path('',views.home_page,name='home_page'),
    path('register/',views.registering_patient,name='register_patient'),
    path('vital/',views.registerVitals,name='vital_checkup') ,
    path('visit/',views.visit_register,name='visitors')
]