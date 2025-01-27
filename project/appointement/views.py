
from django.shortcuts import render, redirect, get_object_or_404

#from .import forms
#from django.contrib.auth import authenticate, login
#from django.contrib.auth.models import  User
from django.contrib.auth.decorators import login_required 
from .import models


def testhtml(request):
    return render(request, "testhtml/test.html")
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""


def index_views(request):
    return render(request,'page/index.html')


#@login_required(login_url='/login/')
def dashboard_views(request):
    appoint=models.Appointement.objects.filter(
        patient__user=request.user,
        status="En attente", 
        )
    
    rv=appoint.count()
    print("Nombre RV:",rv)
    return render(request, 'page/dashboard.html', {"rv":rv})



def list_appointement(request):
    appoint=models.Appointement.objects.filter(patient_id__user=request.user).order_by("-date")
    return render(request, 'page/list_appoint.html', {"appoint":appoint})
    


def add_appointement(request):

    if request.method=="POST":
        title=request.POST.get("title")
        patient_id=request.POST.get("patient_id")
        date=request.POST.get("date")
        time=request.POST.get("time")
        place=request.POST.get("place")
        status=request.POST.get("status")


        patient=get_object_or_404(
                                models.Patient, 
                                id=patient_id, 
                                user=request.user,
                                )
    
        models.Appointement.objects.create(
            title=title,
            patient=patient,
            date=date,
            time=time,
            place=place,
            status=status
        )

        
        return redirect("list_app")
    
    patients=models.Patient.objects.filter(user=request.user)
    
    return render(request, "appoint/add_appoint.html", {"patients":patients})



def update_appoint(request, appoint_id):
    appoint=get_object_or_404(
                models.Appointement, 
                id=appoint_id, 
                patient__user=request.user
                )

    if request.method=="POST":
        title=request.POST.get("title")
        patient_id=request.POST.get("patient_id")
        date=request.POST.get("date")
        time=request.POST.get("time") 
        place=request.POST.get("place")
        status=request.POST.get("status")

        patient=get_object_or_404(
                    models.Patient, 
                    user=request.user, 
                    id=patient_id
                    )

        
        appoint.title=title
        appoint.patient=patient
        appoint.date=date
        appoint.time=time
        appoint.place=place
        appoint.status=status

        appoint.save()

        return redirect("list_app")
    
    patients=appoint.patient

    return render(request, 'appoint/updapp.html', {"appoint":appoint,"patients":patients})


def del_appoint(request, id):
    appoints=get_object_or_404(models.Appointement, id=id)

    if request.method=="POST":
        appoints.delete()
        return redirect("list_app")
    
    return render(request, 'appoint/delapp.html')