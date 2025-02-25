
from pathlib import Path
import os
import environ
from decouple import config
env=environ.Env()   
environ.Env.read_env()  

SECRET_KEY=env('SECRET_KEY')


BASE_DIR = Path(__file__).resolve().parent.parent


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

DEBUG = False


ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost:8080',
    'localhost',

    'gestionnaire-de-rendez-vous-1.onrender.com'
    
                 
                 ]



INSTALLED_APPS = [

    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'appointement.apps.AppointementConfig',
    'patient',
    
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #s'allauth.socialaccount.providers.google',
    

]

ACCOUNT_FORMS = {
    'signup':'account.forms.CustomSignupForm', 
    #'login':'account.forms.CustomSigninForm',
    }



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',
    "allauth.account.middleware.AccountMiddleware",

]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
   
    'django.contrib.auth.backends.ModelBackend',

    'allauth.account.auth_backends.AuthenticationBackend',  
    #'allauth.socialaccount.backends.google.GoogleOAuth2',
    
]


ROOT_URLCONF = 'project.urls'



ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_REQUIRED = True   
ACCOUNT_EMAIL_SUBJECT_PREFIX="Gestionnaire de Rendez-Vous"
ACCOUNT_AUTHENTICATION_METHOD="email"
ACCOUNT_USERNAME_REQUIRED=False
ACCOUNT_CONFIRMATION_EMAIL_ON_GET=True



ACCOUNT_AUTHENTICATED_REDIRECT_URL = '/appoint/board' 
LOGIN_REDIRECT_URL='/appoint/board' 
ACCOUNT_LOGOUT_REDIRECT_URL = "/accounts/login/" 


"""
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
        
    },
}

"""


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



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'  
EMAIL_HOST_PASSWORD = config('SENDGRID_API_KEY') 
DEFAULT_FROM_EMAIL = 'hthierdl70@gmail.com'  


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR ,'staticfiles')
STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static')]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
CSRF_TRUSTED_ORIGINS = [

    'http://localhost:8080',
    'https://gestionnaire-de-rendez-vous-1.onrender.com'


]
