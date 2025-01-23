from django.urls import path
from patient import views

urlpatterns=[
    path('pative',views.patient_view, name="pative"),
    path('addpatient', views.addpatient, name="addpatient"),
    path('updatepat/<int:id>/', views.update_patient, name="updatepat"),
    path('delete/<int:id>/', views.delete_patient, name="delete"),
    #/pat/delete/11/
    ]


#383265770411-khap21ij19uv4210a20epqr5igsecg9c.apps.googleusercontent.com
#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