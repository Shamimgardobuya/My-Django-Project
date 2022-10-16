from unicodedata import name
from django.urls import path
# from .views import home_page
from .views import SearchPatient,home_page,registering_patient,registerVitals,visit_register,visit,patient_dashboard,pivot_data
# from .views import *

urlpatterns=[
    path('',home_page,name='home_page'),
    path('register/',registering_patient,name='register_patient'),
    path('vital/',registerVitals,name='vital_checkup') ,
    path('visit/',visit_register,name='visitors'),
    # path('all/',all_patients,name='all'),
    path("all_visits/",visit,name="all_visits"),
    path('dash/', patient_dashboard, name='dashboard'),
    path('data/',pivot_data, name='pivot_data'),
    path("all/",SearchPatient.as_view(),name='all'),

]