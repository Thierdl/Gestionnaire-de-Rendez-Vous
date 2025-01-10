
from django.shortcuts import render, redirect
from .import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import  User
from .import models


def testhtml(request):
    return render(request, "testhtml/test.html")
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""


def index_views(request):
    return render(request,'page/index.html')

def appointement_views(request):
    #date
    #time
    #name patient
    return render()


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
            place=place
            
        )

        appointement.save()
        return redirect("test")

    return render(request, "appoint/add_appoint.html")


