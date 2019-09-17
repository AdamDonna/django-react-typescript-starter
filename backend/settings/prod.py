"""Use this for production"""

from .base import *  # NOQA

DEBUG = False

# TODO: Add prod host here
# ALLOWED_HOSTS = []

WSGI_APPLICATION = "backend.wsgi.prod.application"

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

STATICFILES_STORAGE = "whitenoise.django.GzipManifestStaticFilesStorage"

SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 604_800
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"
