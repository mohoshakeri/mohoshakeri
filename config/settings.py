from pathlib import Path
import pymysql
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

deploy_status = 'development'
deploy = {
    'development' : {
        'debug' : True,
        'hosts' : ['localhost','10.42.0.1'],
        'static_dir' : [os.path.join(BASE_DIR,'static'),],
        'static_root' : None,
        'url' : 'http://localhost:3000',
        'database' : {
            'host' : 'localhost',
            'user' : 'root',
            'pass' : '',
            'db' : 'mohoshakeri',
            'port' : 4306
                }
    },
    'production' : {
        'debug' : False,
        'hosts' : ['mohoshakeri.ir','www.mohoshakeri.ir'],
        'static_dir' : [],
        'static_root' : os.path.join(BASE_DIR,'static'),
        'url' : 'https://mohoshakeri.ir',
        'database' : {
            'host' : 'localhost',
            'user' : 'root',
            'pass' : '',
            'db' : 'mohoshakeri',
            'port' : 3306
                }
    },
}

SECRET_KEY = 'django-insecure-bfzyd0akr5^!%$7qy@@r1ad$cl08qi3h6-c7usmg8rx6-h(*jw'
DEBUG = deploy[deploy_status]['debug']
ALLOWED_HOSTS = deploy[deploy_status]['hosts']


# Application definition
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
pymysql.install_as_MySQLdb()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': deploy[deploy_status]['database']['db'],
        'USER': deploy[deploy_status]['database']['user'],
        'PASSWORD': deploy[deploy_status]['database']['pass'],
        'HOST': deploy[deploy_status]['database']['host'],
        'PORT': str(deploy[deploy_status]['database']['port']),
    },
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = deploy[deploy_status]['static_dir']
STATIC_ROOT = deploy[deploy_status]['static_root']

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Session
SESSION_SAVE_EVERY_REQUEST = True

# Time
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_TZ = False