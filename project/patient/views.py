from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .import models
<<<<<<< HEAD

=======
from patient.forms import ResearchForm
>>>>>>> deve



@login_required(login_url="/accounts/login/")
def patient_view(request):
    patients=models.Patient.objects.filter(user=request.user).order_by("-created")
    patient_count=patients.count()

    return render(request, "patient/list-patient.html", {
                            "patient_count":patient_count, 
                            "patients":patients,

                            })


@login_required(login_url="/accounts/login/")
def addpatient(request):
    if request.method=="POST":        
        name=request.POST.get("name")
        firstname=request.POST.get("firstname")
        age=request.POST.get("age")
        adress=request.POST.get("adress")
        phone=request.POST.get("phone")

        user=request.user

        patient=models.Patient.objects.create(
            name=name,
            firstname=firstname,
            age=age,
            adress=adress,
            phone=phone,

            user=user,
        )

        patient.save()
        return redirect("list-patient")
    
    return render(request, "patient/addpatient.html")
    

@login_required(login_url="/accounts/login/")
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
        return redirect("list-patient")

    return render(request, "patient/updatepat.html", {'patient':patient})

    
@login_required(login_url="/accounts/login/")
def delete_patient(request, id):
    patients=get_object_or_404(models.Patient, id=id)

    if request.method=="POST":
        patients.delete()

        return redirect("list-patient")
    return render(request, {"patients":patients})



def research_patient(request):
    form = ResearchForm(request.GET)
    patient=[]

    if form.is_valid():
        query=form.cleaned_data['query']
        patient=models.Patient.objects.filter(name__icontains=query)|models.Patient.objects.filter(firstname__icontains=query)

    return render(request, 'page/research.html', {"patient":patient, "form":form})


