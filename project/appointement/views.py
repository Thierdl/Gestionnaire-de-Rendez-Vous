
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



@login_required(login_url='/login/')
def dashboard_views(request):
    return render(request, 'page/dashboard.html')



def list_appointement(request):
    appoint=models.Appointement.objects.all()
    return render(request, 'page/list_appoint.html', {"appoint":appoint})



def add_appointement(request):
    if request.method=="POST":
        title=request.POST.get("title")
        patient=request.POST.get("patient")
        date=request.POST.get("date")
        time=request.POST.get("time")
        place=request.POST.get("place")

        appointement=models.Appointement.objects.create(
            title=title,
            patient=patient,
            date=date,
            time=time,
            place=place,  
        )

        appointement.save()
        return redirect("list_app")

    return render(request, "appoint/add_appoint.html")



def update_appoint(request, id):
    appoint=get_object_or_404(models.Appointement, id=id)

    if request.method=="POST":
        title=request.POST.get("title")
        patient=request.POST.get("patient")
        date=request.POST.get("date")
        time=request.POST.get("time") 
        place=request.POST.get("place")

        appoint.title=title
        appoint.patient=patient
        appoint.date=date
        appoint.time=time
        appoint.place=place

        appoint.save()

        return redirect("list_app")
    return render(request, 'appoint/updapp.html', {"appoint":appoint})


def del_appoint(request, id):
    appoints=get_object_or_404(models.Appointement, id=id)

    if request.method=="POST":
        appoints.delete()
        return redirect("list_app")
    
    return render(request, 'appoint/delapp.html')