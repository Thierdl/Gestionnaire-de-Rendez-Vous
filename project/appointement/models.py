from django.db import models

class Patient(models.Model):
    name=models.CharField(max_length=59)
    firstname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    age=models.IntegerField()
    adress=models.CharField(max_length=55)
    phone=models.IntegerField()

    def __str__(self):
        return self.name
    

class Appointement(models.Model):
    title=models.CharField(max_length=50)
    patient=models.CharField(max_length=50)
    date=models.DateField()
    time=models.TimeField()
    place=models.CharField(max_length=50)

    patient=models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointement')

    def __str__(self):
        return f"{self.title}"