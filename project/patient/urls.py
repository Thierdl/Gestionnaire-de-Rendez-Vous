from django.urls import path
from patient import views

urlpatterns=[
    path('addpatient', views.addpatient, name="addpatient"),

    ]