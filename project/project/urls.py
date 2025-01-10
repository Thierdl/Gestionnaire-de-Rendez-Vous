
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import AppointementViewSet, PatientViewSet



route=routers.SimpleRouter()
route.register('appointement',AppointementViewSet, basename='appointement')
route.register('patient', PatientViewSet, basename='patient')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
    path('appoit/',include('appointement.urls')),
    path('pat/', include("patient.urls")),
    path('', include('account.urls')),
   
]
