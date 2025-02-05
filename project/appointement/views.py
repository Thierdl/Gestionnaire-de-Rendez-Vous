
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from .import models

from patient.models import Patient

def index_views(request):
    return render(request,'page/index.html')


@login_required(login_url="/login/")
def confirmed(request):
    confirmed=models.Appointement.objects.filter(patient__user=request.user, status="Confirmer")
    return render(request, "list/confirmed.html", {"confirmed":confirmed})


@login_required(login_url="/login/")
def on_hold(request):
    on_hold=models.Appointement.objects.filter(patient__user=request.user, status="En attente")
    return render(request, "list/on_hold.html", {"on_hold":on_hold})


@login_required(login_url="/login/")
def cancel(request):
    cancel=models.Appointement.objects.filter(patient__user=request.user, status="Annuler")
    return render (request, "list/cancel.html", {"cancel":cancel})



@login_required(login_url='/login/')
def dashboard_views(request):
    appoint=models.Appointement.objects.filter(patient__user=request.user)
    on_hold=models.Appointement.objects.filter(patient__user=request.user, status="En attente")
    confirmed=models.Appointement.objects.filter(patient__user=request.user, status="Confirmer")
    cancel=models.Appointement.objects.filter(patient__user=request.user, status="Annuler")

    patient=Patient.objects.filter(user=request.user)
    
    rv=appoint.count()
    on_holds=on_hold.count()
    patients=patient.count()
    confirmeds=confirmed.count()
    cancels=cancel.count()
    
    return render(request, "page/dashboard.html", {
                            "rv":rv,
                            "patients":patients, 
                            "on_holds":on_holds,
                            "confirmeds":confirmeds,
                            "cancels":cancels,
                            }
                        )

@login_required(login_url='/login/')
def list_appointement(request):
    appoint=models.Appointement.objects.filter(
                        patient_id__user=request.user 
                        ).order_by("-date")
    
    return render(request, 'page/list_appoint.html', {"appoint":appoint})
    

@login_required(login_url='/login/')
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
            status=status,
        )

        
        return redirect("list_appoint")
    
    patients=models.Patient.objects.filter(user=request.user)
    
    
    return render(request, "appoint/add_appoint.html", {"patients":patients})


@login_required(login_url='/login/')
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

        return redirect("list_appoint")
    
    patients=models.Patient.objects.filter(user=request.user)

    return render(request, 'appoint/updapp.html', {
                                "appoint":appoint,
                                "patients":patients
                                }
                            )

@login_required(login_url='/login/')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
def del_appoint(request, appoint_id):
    appoints=get_object_or_404(
                        models.Appointement, 
                        id=appoint_id, 
                        patient__user=request.user
                        )

    if request.method=="POST":
        appoints.delete()
        return redirect("list_app")
    
    return render(request, 'appoint/updapp.html')