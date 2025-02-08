
from pathlib import Path
import os
import environ

env=environ.Env()   
environ.Env.read_env()  

SECRET_KEY=env('SECRET_KEY')

BASE_DIR = Path(__file__).resolve().parent.parent

"""
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = env('GOOGLE_CLIENT_ID')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = env('GOOGLE_CLIENT_SECRET')
"""


"""
DATABASES={
    'default':env.db('DATABASE_URL', default='sqlite:///{}'.format(BASE_DIR / 'db.sqlite3')),
}
"""


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/mnt/data/db.sqlite3',  
        'OPTIONS': {
            'timeout': 20,
        }
    }
}



SESSION_COOKIE_NAME = 'sessionid_{}'.format(os.getpid())

DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost:8080',
    'localhost',
    '2a33-196-207-227-140.ngrok-free.app',
    #'https://gestionnaire-de-rendez-vous.onrender.com',
                 
                 ]


# Application definition

INSTALLED_APPS = [

    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'appointement',
    'patient',
    'debug_toolbar',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #s'allauth.socialaccount.providers.google',
    'sendmail',

    'crispy_forms',
    'crispy_bootstrap4',
    
]


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

CRISPY_TEMPLATE_PACK = "bootstrap4"



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    "allauth.account.middleware.AccountMiddleware",

]

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
   
    'django.contrib.auth.backends.ModelBackend',

    'allauth.account.auth_backends.AuthenticationBackend',  
    #'allauth.socialaccount.backends.google.GoogleOAuth2',
    
]


ROOT_URLCONF = 'project.urls'

LOGIN_REDIRECT_URL='/appoint/board' #

ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_REQUIRED = True   #

ACCOUNT_LOGOUT_REDIRECT_URL = "/accounts/login/" #



GOOGLE_CLIENT_ID='74664223955-4tn4e5fag58eu69gme86iu0foc1oulpb.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET='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'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {'access_type': 'online'},
        'OAUTH_PKCE_ENABLED': True,
        #'REDIRECT_URI': 'https://2a33-196-207-227-140.ngrok-free.app/accounts/google/login/callback/',
        
    },
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'  # Utilise le mot 'apikey' ici
EMAIL_HOST_PASSWORD = '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'  # Ta clé API générée par SendGrid
DEFAULT_FROM_EMAIL = 'hthierdl70@gmail.com'  # Ton adresse email par défaut


INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',  
]




TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]





WSGI_APPLICATION = 'project.wsgi.application'



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'
#STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static')]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8080',
    'https://2a33-196-207-227-140.ngrok-free.app',
    #'83cb-196-207-227-140.ngrok-free.app',
]


