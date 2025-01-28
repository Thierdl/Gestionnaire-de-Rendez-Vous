from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="patient")

    name=models.CharField(max_length=59)
    firstname=models.CharField(max_length=50)
    age=models.PositiveIntegerField()
    adress=models.CharField(max_length=55)
    phone=models.IntegerField(blank=True)

    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
