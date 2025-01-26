'''import os
import pickle
import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Si vous modifiez cette portée, supprimez le fichier token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def authenticate_gmail():
    """Authentifie et retourne le service Gmail."""
    creds = None
    # Le fichier token.pickle stocke les tokens d'accès de l'utilisateur et est créé automatiquement lors du processus d'authentification.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # Si les credentials sont invalides ou n'existent pas, nous demandons à l'utilisateur de se connecter.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Sauvegarde les credentials pour la prochaine utilisation.
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    # Build du service Gmail.
    service = build('gmail', 'v1', credentials=creds)
    return service
'''