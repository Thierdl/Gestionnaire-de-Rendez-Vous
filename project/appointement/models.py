from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient

class Appointement(models.Model):
    
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="appointement")
    
    title=models.CharField(max_length=50)
    date=models.DateField(null=True, blank=True)
    time=models.TimeField(null=True, blank=True)
    place=models.CharField(max_length=50)
    status=models.CharField(max_length=20, choices=[
        ("En attente","En attente"),
        ("Confirmer","Confirmer"),
        ("Annuler","Annuler")
    ],
    default="En attente",
                            )
    
    created=models.DateTimeField(auto_now_add=True) 

    #if status > now
    #else:
    #    return

    def __str__(self):
        return f"{self.title}"