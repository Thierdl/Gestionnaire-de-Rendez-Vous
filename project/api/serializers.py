from rest_framework.serializers import ModelSerializer
from appointement.models import Appointement, Patient

class AppointementSerializer(ModelSerializer):
    class Meta():
        model=Appointement
        fields='__all__'


class PatientSerializer(ModelSerializer):
    class Met():
        model=Patient
        fields='__all__'
