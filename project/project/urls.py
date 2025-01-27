
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from api.views import AppointementViewSet, PatientViewSet
from django.contrib.auth import views as auth_views

from django.conf import settings


route=routers.SimpleRouter()
route.register('appointement',AppointementViewSet, basename='appointement')
route.register('patient', PatientViewSet, basename='patient')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
    path('appoint/',include('appointement.urls')),
    path('pat/', include("patient.urls")),
    #path('accounts/', include('account.urls')),

    path('account/', include('allauth.urls')),


    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(next_page='page1'), name='logout'),

   
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



