import os
import logging
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# For Loging
SECRET_KEY = '_*jgo)*hj8qf6y0x87hcu*w6lng@5*w#6rs_pe+5l=_8m2(_gq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appauth',
    'edu',
    'apiauth',
    'apiedu',
    'hrm',
    'apihrm',
    'crispy_forms',
    'rest_framework',
]

# Django API Permition
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ]

}

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'education.urls'

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

WSGI_APPLICATION = 'education.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'education',
#         'USER': 'postgres',
#         'PASSWORD': 'mahabub77',
#         'HOST': 'localhost',
#         'PORT': '5432',
#         'ATOMIC_REQUESTS': True,
#     }
# }



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'education',
        'USER': 'education',
        'PASSWORD': 'education',
        'HOST': 'localhost',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True,
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
# '''

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
log_file = "D:\\Projects\\education1\\application_logs.log"
# log_file="/webadmin/demofinance/logs/application_logs.log"
# print(log_file)
logging.basicConfig(format='%(asctime)s  %(levelname)-8s [%(name)s: %(lineno)d]  %(message)s',
                    datefmt='%d-%m-%Y:%H:%M',
                    level=logging.ERROR, filename=log_file)


########
#############Image Location #############

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

########

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

#DATE_FORMAT ='%Y-%m-%d'

DATE_FORMAT = '%d-%m-%Y'
DATETIME_FORMAT = '%d-%m-%Y %I:%M'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

#SECURE_HSTS_SECONDS = 60
#SECURE_CONTENT_TYPE_NOSNIFF = True
#SECURE_BROWSER_XSS_FILTER = True
#SECURE_SSL_REDIRECT = True
#SESSION_COOKIE_SECURE = True
#SECURE_HSTS_INCLUDE_SUBDOMAINS =True
#SECURE_HSTS_PRELOAD = True
#X_FRAME_OPTIONS = 'DENY'
#SECURE_HSTS_PRELOAD = True
#CSRF_COOKIE_SECURE = True