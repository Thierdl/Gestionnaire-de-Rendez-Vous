
from django.urls import path
from appointement import views

urlpatterns = [
    
    path('index', views.index_views, name="index"),
    
    path('board', views.dashboard_views, name="board"),
         
    path('test',views.testhtml,  name="test"),
    path('add', views.add_appointement, name="add"),
    
]
