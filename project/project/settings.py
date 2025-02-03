
from pathlib import Path
import os
import environ

env=environ.Env()   
environ.Env.read_env()  

#client_id='860432862760-cic1tvt36noa9ge3hkvanca5u4788utk.apps.googleusercontent.com'
#secret_key='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'


SECRET_KEY=env('SECRET_KEY')

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES={
    'default':env.db('DATABASE_URL', default='sqlite:///{}'.format(BASE_DIR / 'db.sqlite3')),
}

SESSION_COOKIE_NAME = 'sessionid_{}'.format(os.getpid())

DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '1f26-41-82-151-36.ngrok-free.app'
                 
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
    'allauth.socialaccount.providers.google',

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
    
]


ROOT_URLCONF = 'project.urls'

LOGIN_REDIRECT_URL='/appoint/board' 

ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_REQUIRED = True
#ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

#ACCOUNT_USERNAME_REQUIRED = False 
ACCOUNT_LOGOUT_REDIRECT_URL = "/accounts/login/"



"""
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

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id':'860432862760-cic1tvt36noa9ge3hkvanca5u4788utk.apps.googleusercontent.com',  
            'secret':'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',  
            'key': ''
        },
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}



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





