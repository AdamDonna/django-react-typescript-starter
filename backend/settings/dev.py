"""Use this for development"""

from .base import *  # NOQA

DEBUG = True

WSGI_APPLICATION = "backend.wsgi.dev.application"

CORS_ORIGIN_WHITELIST = ["http://localhost:3000"]
