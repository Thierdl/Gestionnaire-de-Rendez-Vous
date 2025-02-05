from django.urls import path
from .import views

urlpatterns=[
    #path('login/',views.login_view, name="login"),
    #path('signup/',views.signup_view, name="signup"),
    #path('send-test-email/', views.send_test_email, name='send_test_email'),
    path('send-test-email/', views.send_test_email, name='send_test_email'),
]

# urls.py

