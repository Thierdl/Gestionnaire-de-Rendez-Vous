
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from api.views import AppointementViewSet, PatientViewSet

from django.conf import settings


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


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]


