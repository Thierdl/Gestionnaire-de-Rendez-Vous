'''
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from .import forms


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



# views.py

from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

def send_test_email(request):
    # Envoie un email de test
    subject = 'Test Email'
    message = 'Ceci est un test d\'envoi d\'email depuis Django.'
    recipient_list = ['ton_adresse_email@gmail.com']  # Remplace par ton adresse email

    # Envoi de l'email
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

    return HttpResponse("Email envoyé avec succès !")
'''


# views.py
from django.core.mail import send_mail
from django.http import HttpResponse

def send_test_email(request):
    subject = 'Test d\'envoi d\'e-mail avec SendGrid'
    message = 'Ceci est un message de test envoyé depuis Django avec SendGrid.'
    from_email = 'ton_email@domaine.com'  
    recipient_list = ['destinataire@example.com']  
    try:
        send_mail(subject, message, from_email, recipient_list)
        return HttpResponse("E-mail envoyé avec succès !")
    except Exception as e:
        return HttpResponse(f"Erreur lors de l'envoi de l'e-mail : {str(e)}")

