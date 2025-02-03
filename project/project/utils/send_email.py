import sendgrid
from sendgrid.helpers.mail import Mail, Email, Content

SENDGRID_API_KEY = "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"

def send_email(to_email, subject, content):
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    
    # Création de l'email 
    from_email = Email("hthierdl70@gmail.com")  
    to_email_obj = Email(to_email)  

    # Création du contenu HTML
    content = Content("text/html", content)  

    # Création de l'objet email
    email = Mail(from_email, subject, to_email_obj, content)

    try:
        # Envoi de l'email via SendGrid
        response = sg.client.mail.send.post(request_body=email.get())
        print(f"Email envoyé avec le statut : {response.status_code}")
        return response.status_code
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email : {e}")
        return str(e)

# Test de l'envoi
send_email("albertmangua410@gmail.com", "Test SMTP avec SendGrid", "<p>CONTENU HTML</p>")