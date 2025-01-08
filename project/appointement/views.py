from rest_framework.viewsets import ModelViewSet

from .serializers import AppointementSerializer, PatientSerializer
from .models import Appointement, Patient
from django.shortcuts import render


def index_views(request):
    return render(request,'page/index.html')

def signup_views(request):
    return render(request, 'account/signup.html')


class AppointementViewSet(ModelViewSet):
    serializer_class=AppointementSerializer

    def get_queryset(self):
        queryset=Appointement.objects.all()
        return queryset


class PatientViewSet(ModelViewSet):
    serializer_class=PatientSerializer

    def  get_queryset(self):
        queryset=Patient.objects.all()
        return queryset
