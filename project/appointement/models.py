from django.db import models
from patient.models import Patient


class Appointement(models.Model):

    patient=models.ForeignKey(
                            Patient, 
                            on_delete=models.CASCADE, 
                            related_name="appointement",
            )
    
    title=models.CharField(max_length=50)
    date=models.DateField()
    time=models.TimeField()
    place=models.CharField(max_length=50)
    status=models.CharField(max_length=20, choices=[

        ("En attente","En attente"),
        ("Confirmer","Confirmer"),
        ("Annuler","Annuler")
    ],
    default="En attente",
                            )
    

    def __str__(self):
        return f"{self.title}"
   