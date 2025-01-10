from django.db import models

class Patient(models.Model):
    name=models.CharField(max_length=59)
    firstname=models.CharField(max_length=50)
    age=models.IntegerField()
    adress=models.CharField(max_length=55)
    phone=models.IntegerField(int)

    def __str__(self):
        return self.name
    

class Appointement(models.Model):
    title=models.CharField(max_length=50)
    patient=models.CharField(max_length=50)
    date=models.DateField(null=True, blank=True)
    time=models.TimeField(null=True, blank=True)
    place=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title}"