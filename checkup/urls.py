from unicodedata import name
from django.urls import path
# from .views import home_page
from . import views

from .views import all_patients, home_page,registering_patient,registerVitals,visit_register,visit,patient_dashboard,pivot_data
# from .views import *

urlpatterns=[
    path('home/',home_page,name='home_page'),
    path('register/',registering_patient,name='register_patient'),
    path('vital/',registerVitals,name='vital_checkup') ,
    path('visit/',visit_register,name='visitors'),
    # path('all/',all_patients,name='all'),
    path("all_visits/",visit,name="all_visits"),
    path('dash/', patient_dashboard, name='dashboard'),
    path('data/',pivot_data, name='pivot_data'),
    path("all/",all_patients,name='all'),
    path('',views.register,name='registerUser'),
    path("login/", views.login_request, name="login")
   

]

