import os  # Bu qator settings.py boshida bo'lishi kerak.
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'YOUR_ACTUAL_SECRET_KEY'  #  <--- MAXFIY KALITNI QO'YING!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  # PRODUCTION UCHUN FALSE

ALLOWED_HOSTS = ['diplomatseyf.uz', 'www.diplomatseyf.uz', '127.0.0.1', 'localhost']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'safebox_app',  # Ilovangiz
    'rest_framework',  # Agar API ishlatsangiz
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Whitenoise, to'g'ri joyda
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'safebox_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'safebox_app.context_processors.categories',  # Agar context_processors.py ichida categories funksiyangiz bo'lsa
            ],
        },
    },
]

WSGI_APPLICATION = 'safebox_project.wsgi.application'

# Database (SQLite, cPanel-da o'zgartirish shart emas)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation (ixtiyoriy)
AUTH_PASSWORD_VALIDATORS = []

# Internationalization (til sozlamalari)
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

# Whitenoise sozlamasi (BU JUDA MUHIM!)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# STATICFILES_DIRS NI O'CHIRING, agar faqat app ichidagi static papkalardan foydalansangiz
# STATICFILES_DIRS = [
#     BASE_DIR / "assets", # Agar assets papkangiz bo'lsa, va u django papkasi ichida bo'lsa.
# ]


# staticfiles papkasining serverdagi manzili:
STATIC_ROOT = BASE_DIR / 'staticfiles'  # BU TO'G'RI (agar staticfiles django ichida bo'lsa)


# Media files (yuklanadigan fayllar, rasmlar)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media' #  /home/diploma4/public_html/django/media


# Login URL (agar kerak bo'lsa)
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home' #  login bo'lgandan keyingi manzil
LOGOUT_REDIRECT_URL = 'home'# logout bo'lgandan keyingi manzil