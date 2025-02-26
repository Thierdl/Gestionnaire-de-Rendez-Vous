from django.urls import path
from patient import views

urlpatterns=[
    path('list-patient',views.patient_view, name="list-patient"),
    path('addpatient', views.addpatient, name="addpatient"),
    path('updatepat/<int:id>/', views.update_patient, name="updatepat"),
    path('delete/<int:id>/', views.delete_patient, name="delete"),
    path('recherche', views.research_patient, name="recherche"),
     
    ]

