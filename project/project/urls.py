
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from appointement.views import AppointementViewSet, PatientViewSet
from appointement.views import index_views

route=routers.SimpleRouter()
route.register('appointement',AppointementViewSet, basename='appointement')
route.register('patient', PatientViewSet, basename='patient')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',include('appointement.urls')),
    path('api/', include(route.urls))
]
