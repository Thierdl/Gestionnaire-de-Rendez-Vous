
from django.shortcuts import render, redirect
from .import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import  User



def index_views(request):
    return render(request,'page/index.html')

def add_appointement(request):
    return

def update_appointement(request):
    return

def delete_appointement(request):
    return
