
from django.urls import path
from .views import index_views, signup_views

urlpatterns = [
    path('', index_views),
    path('signup',signup_views),
]
