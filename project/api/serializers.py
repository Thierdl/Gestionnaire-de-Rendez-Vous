from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from appointement.models import Appointement
from patient.models import Patient


class UserSerializer(ModelSerializer):
    class Meta():
        model=User
        fields = ['url', 'username', 'email', 'password', 'groups']


class AppointementSerializer(ModelSerializer):
    class Meta():
        model=Appointement
        fields='__all__'


class PatientSerializer(ModelSerializer):
    class Meta():
        model=Patient
        fields='__all__'
