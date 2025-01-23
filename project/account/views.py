from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from .import forms

"""
def login_view(request):
  form=forms.Login(request.POST or None)
  user=""

 
  if form.is_valid():
    username=form.cleaned_data.get("username")
    password=form.cleaned_data.get("password")
  
    user=authenticate(username=username, password=password)
      
    if user is not None:
      login(request, user)
      return redirect("board")
    
  return render(request, "account/login.html", {"form":form,"user":user})
    


def signup_view(request):
  if request.method=="POST":

    form=forms.Signup(request.POST or None)

    if form.is_valid():
      name=form.cleaned_data.get("name")
      firtsname=form.cleaned_data.get("firtsname")
      username=form.cleaned_data.get("username")
      password=form.cleaned_data.get("password")

      user=User.objects.create_user(
          name=name,
          firtsname=firtsname,
          username=username,
          password=password,
          
      )

      user=authenticate(
          name=name,
          firtsname=firtsname,
          username=username,
          password=password
      )

      login(request, user)
      return redirect("index")
  else:
    form = forms.Signup()

  return render(request, "account/signup.html", {"form":form})
"""