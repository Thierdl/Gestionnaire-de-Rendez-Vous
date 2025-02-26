
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from api.views import AppointementViewSet, PatientViewSet, UserViewSet
from django.contrib.auth import views as auth_views





route=routers.SimpleRouter()
route.register('appointement',AppointementViewSet, basename='appointement')
route.register('patient', PatientViewSet, basename='patient')

router = routers.DefaultRouter()
router.register('user', UserViewSet, basename="user")





urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(route.urls)),
    path('apis/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

    path('appoint/',include('appointement.urls')),
    path('patient/', include("patient.urls")),
    #path('account/', include('account.urls')),
   
    path('accounts/', include('allauth.urls')),

]

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


"""
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

"""

