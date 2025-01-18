from django.urls import path
from patient import views

urlpatterns=[
    path('pative',views.patient_view, name="pative"),
    path('addpatient', views.addpatient, name="addpatient"),
    path('updatepat/<int:id>/', views.update_patient, name="updatepat"),
    path('delete/<int:id>/', views.delete_patient, name="delete"),
    #/pat/delete/11/
    ]