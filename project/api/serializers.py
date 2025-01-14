from rest_framework.serializers import ModelSerializer
from appointement.models import Appointement
from patient.models import Patient

class AppointementSerializer(ModelSerializer):
    class Meta():
        model=Appointement
        fields='__all__'


class PatientSerializer(ModelSerializer):
    class Meta():
        model=Patient
        fields='__all__'
