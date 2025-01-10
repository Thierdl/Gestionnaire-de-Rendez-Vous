from django.db import models

class Patient(models.Model):
    name=models.CharField(max_length=59)
    firstname=models.CharField(max_length=50)
    age=models.IntegerField()
    adress=models.CharField(max_length=55)
    phone=models.IntegerField(int)

    def __str__(self):
        return self.name
    
