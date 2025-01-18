
from django.urls import path
from appointement import views

urlpatterns = [
    
    path('index', views.index_views, name="index"),
    path('board', views.dashboard_views, name="board"),
    path('list_app', views.list_appointement, name="list_app"),
    path('add_app', views.add_appointement, name="add_app"),
    #path('upd_app'),
        
    path('test',views.testhtml,  name="test"),
    path('add', views.add_appointement, name="add"),
    
]
