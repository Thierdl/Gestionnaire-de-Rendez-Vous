from rest_framework import serializers

from .models import Appointement, Patient

class AppointementSerializer(serializers.ModelSerializer):
    class Meta():
        model=Appointement
        fields='__all__'


class PatientSerializer(serializers.ModelSerializer):
    class Meta():
        model=Patient
        fields='__all__'

        