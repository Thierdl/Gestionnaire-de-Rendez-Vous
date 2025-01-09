from rest_framework.viewsets import ModelViewSet
from .serializers import AppointementSerializer, PatientSerializer
from appointement.models import Appointement, Patient

class AppointementViewSet(ModelViewSet):
    serializer_class=AppointementSerializer

    def get_queryset(self):
        queryset=Appointement.objects.all()
        return queryset
    
    def get_queryset(self):
        queryset=Patient.object.all()
        return queryset
        