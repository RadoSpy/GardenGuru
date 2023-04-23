import socket
from .base_settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True


db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)