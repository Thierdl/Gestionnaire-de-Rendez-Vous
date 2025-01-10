from django.shortcuts import render, redirect
from .import models
# Create your views here.

def patient_view(request):
    return render()

def addpatient(request):
    if request.method=="POST":        
        name=request.POST.get("name")
        firstname=request.POST.get("firstname")
        age=request.POST.get("age")
        adress=request.POST.get("adress")
        phone=request.POST.get("phone")

        patient=models.Patient.objects.create(
            name=name,
            firstname=firstname,
            age=age,
            adress=adress,
            phone=phone,
        )

        patient.save()
        return redirect("test")
    
    return render(request, "patient/addpatient.html")

def update(request):
    return render(request)

def delete(request):
    return render()
