from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework import viewsets, permissions
from .serializers import AppointementSerializer, PatientSerializer, UserSerializer
from appointement.models import Appointement
from patient.models import Patient


class UserViewSet(ViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()



class UserViewSet(viewsets.ModelViewSet):
   
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
   

class AppointementViewSet(ModelViewSet):
    serializer_class=AppointementSerializer

    def get_queryset(self):
        queryset=Appointement.objects.filter(status="Annuler")
        qs = Appointement.objects.filter(status="Confirmer")
        qx = Appointement.objects.filter(status="En attente")
        

        combined_queryset=queryset |  qs | qx
        return combined_queryset.order_by("-date")
    


#    def get_queryset(self, *args, **kwargs):
#        qs = Appointement.objects.all()
#        qs = qs.filter(owner=self.request.user)
#        return qs



#    def get_queryset(self):
#        queryset=Appointement.objects.all()
#        return queryset
    


    

   
    
    
class PatientViewSet(ModelViewSet):
    serializer_class=PatientSerializer
    
    def get_queryset(self):
        queryset=Patient.objects.all()
        return queryset
            