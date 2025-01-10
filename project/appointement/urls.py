
from django.urls import path
from appointement import views

urlpatterns = [
    
    path('', views.index_views, name="index"),
    
    path('test',views.testhtml,  name="test"),
    path('add', views.add_appointement, name="add"),
    
]
