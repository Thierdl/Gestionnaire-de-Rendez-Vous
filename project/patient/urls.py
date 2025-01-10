from django.urls import path
from patient import views

urlpatterns=[
    path('pative',views.patient_view, name="pative"),
    path('addpatient', views.addpatient, name="addpatient"),
    path('updatepat', views.update_patient, name="updatepat"),


    ]