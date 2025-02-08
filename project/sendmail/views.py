
from django.http import HttpResponse
from .gmail_auth import authenticate_gmail, send_email


def send_test_email(request):
    # Authentifier l'application
    service = authenticate_gmail()

    sender = 'hthierdl70@gmail.com'
    recipient = 'rossumguido76@gmail.com'
    subject = 'Test Email'
    body = 'Ceci est un email envoyé via l\'API Gmail.'

    # Envoyer l'email
    send_email(service, sender, recipient, subject, body)
    
    return HttpResponse("Test email envoyé avec succès via Gmail API!")

