from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-)dn2mf5zka5gfl+!*c_9j0caob925!glpn6p)8r3dgcq!o(lzk'

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

DEBUG = os.environ.get("DEBUG")
# DEBUG = True  # Set to False in production
SECRET_KEY = os.environ.get("SECRET_KEY")

# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")
ALLOWED_HOSTS = ["*"]


# ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # channels
    "channels",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # internal apps
    "apps.core",
    "apps.postsapi",
    # "api",
    "apps.accounts",
    "apps.like",
    "apps.comments",
    "apps.search",
    #  do i need to use this as a separate app? or not think it later.
    "common.pagination",
    "notifications",
    # third party apps
    "drf_spectacular",
    # external apps
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # corse header
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "apitesting.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "apitesting.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

# AUTH_USER_MODEL = "api.User"  # 'api' should be the name of your app
AUTH_USER_MODEL = (
    "accounts.User"  # "accounts.User"  # 'accounts' should be the name of your app
)

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "tiktokapi",  # database name
#         "USER": "admin",
#         "PASSWORD": "admin",
#         "HOST": "localhost",
#         "PORT": "5432",
#     }
# }

# from railway
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT"),  # Default PostgreSQL port
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

# STATIC_URL = "static/"

STATIC_URL = "static/"
# STATIC_ROOT = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # For collectstatic


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",  # Add your frontend's URL
#     "http://127.0.0.1:3000",  # If you're using localhost
# ]

# Allow headers and methods if needed:
# CORS_ALLOW_HEADERS = ['*']
# CORS_ALLOW_METHODS = ['GET', 'POST', 'OPTIONS']

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

# Allow credentials (e.g., cookies, Authorization headers)
CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = [
    # "http://localhost:3000",  # Frontend origin
    # "http://127.0.0.1:3000",  # Frontend origin
    "https://web-production-9fcc5.up.railway.app",
]

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "https://web-production-9fcc5.up.railway.app",
]

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = "None"
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = "None"

# settings.py
CORS_ALLOWED_ORIGINS = [
    # "http://localhost:3000",  # or 127.0.0.1 if needed
    "https://web-production-9fcc5.up.railway.app",
]


# Optional: Allow all HTTP methods
CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS",
]

SESSION_COOKIE_SAMESITE = "Lax"  # or "None" if HTTPS
SESSION_COOKIE_SECURE = False  # True only in HTTPS
CSRF_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_SECURE = False


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        # "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.UserRateThrottle",
        "rest_framework.throttling.AnonRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "user": "10/hour",  # Customize rate limits
        "anon": "10/minute",
    },
}


# Step 1: Configure Django to Use File-Based Caching
# Add the following configuration to your settings.py file to enable file-based caching in a dedicated folder:

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": os.path.join(BASE_DIR, "cache"),  # Cache directory
        "TIMEOUT": 30000,  # Default timeout for cache (in seconds)
        "OPTIONS": {
            "MAX_ENTRIES": 10000,  # Maximum number of cache entries
            "CULL_FREQUENCY": 3,  # Cull a third of entries when limit is hit
        },
    }
}

# drf specatacular
# Step 2: Configure Django REST Framework to Use Spectacular for OpenAPI Schema Generation
# Add the following configuration to your settings.py file to enable Spectacular for OpenAPI schema generation:
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}


CHANNEL_LAYERS = {"default": {"BACKEND": "channels.layers.InMemoryChannelLayer"}}
