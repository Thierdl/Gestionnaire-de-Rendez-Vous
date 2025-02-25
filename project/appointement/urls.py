
from django.urls import path
from appointement import views

urlpatterns = [
   
    path('',views.redirect_index),
    path('index', views.index_views, name="index"),
    path('board', views.dashboard_views, name="board"),
    path('list_appoint', views.list_appointement, name="list_appoint"),
    path('confirmed', views.confirmed, name="confirmed"),
    path('on_hold',views.on_hold, name="on_hold"),
    path('cancel',views.cancel, name="cancel"),

    path('add_app', views.add_appointement, name="add_app"),

    path('upd_app/<int:appoint_id>/', views.update_appoint, name="upd_app"),
    path('del_app/<int:appoint_id>/', views.del_appoint, name="del_app"),
    
    
]
