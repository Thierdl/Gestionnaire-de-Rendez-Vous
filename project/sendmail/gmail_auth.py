import os
import pickle
import google.auth
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Le fichier credentials.json téléchargé depuis Google Cloud Console
CLIENT_SECRET_FILE = 'credentials.json'
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def authenticate_gmail():
    creds = None
    # Le token est stocké sous forme de fichier local pour réutilisation.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # Si aucune (valid) crédentiale n'est trouvée, on demande à l'utilisateur de s'authentifier.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        # Sauvegarder les credentials pour une utilisation future
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    # Construire le service Gmail API
    service = build('gmail', 'v1', credentials=creds)
    return service


def create_message(sender, to, subject, body):
    #Crée le message MIME pour l'email
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    # Attacher le corps du message
    msg = MIMEText(body)
    message.attach(msg)

    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
    return raw_message

def send_email(service, sender, to, subject, body):
    #Envoie un email via l'API Gmail
    try:
        message = create_message(sender, to, subject, body)
        message = service.users().messages().send(userId="me", body={'raw': message}).execute()
        print(f'Email envoyé à {to}, ID du message: {message["id"]}')
    except Exception as error:
        print(f'Erreur lors de l\'envoi de l\'email: {error}')
