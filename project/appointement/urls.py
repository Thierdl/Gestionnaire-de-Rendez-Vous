
from django.urls import path
from appointement import views

urlpatterns = [
    path('test',views.testhtml,  name="test"),
    path('', views.index_views, name="index"),
    path('add', views.add_appointement, name="add"),
    path('patient', views.add_patient, name="patient")
    
]
