from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .import models
# Create your views here.

def patient_view(request):
    patient=models.Patient.objects.all()
    return render(request, "page/dashboard.html", {'patient':patient})

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
        return redirect("pative")
    
    return render(request, "patient/addpatient.html")
    


def update_patient(request, id):
    patient=get_object_or_404(models.Patient, id=id)
    if request.method=="POST":

        name=request.POST.get("name")
        firstname=request.POST.get("firstname")
        age=request.POST.get("age")
        adress=request.POST.get("adress")
        phone=request.POST.get("phone")

        patient.name=name
        patient.firstname=firstname
        patient.age=age
        patient.adress=adress
        patient.phone=phone

        patient.save()
        return redirect("pative")

    return render(request, "patient/updatepat.html", {'patient':patient})

    



def delete_patient(request, id):
    patients=get_object_or_404(models.Patient, id=id)

    if request.method=="POST":
        patients.delete()

        return redirect("pative")
    return render(request, 'patient/deletepat.html')
