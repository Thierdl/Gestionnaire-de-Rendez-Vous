from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient
from datetime import datetime, date
from django.core.exceptions import ValidationError

class Appointement(models.Model):
    
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="appointement")
    
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
    
"""created=models.DateTimeField(auto_now_add=True) 

    def clean(self):
            today = date.today()  # La date actuelle
            now = datetime.now().time()  # L'heure actuelle

            # Comparer la date de l'appointement avec la date actuelle
            if self.date < today:
                raise ValidationError("La date ne doit pas être inférieure à la date actuelle.")

            # Comparer l'heure si la date est aujourd'hui
            if self.date == today and self.time <= now:
                raise ValidationError("Veuillez choisir une heure supérieure à l'heure actuelle.")
            
    def save(self, *args, **kwargs):
        self.clean()  # Appelle la méthode de validation
        super().save(*args, **kwargs)

"""
    #if status > now
    #else:
    #    return

    