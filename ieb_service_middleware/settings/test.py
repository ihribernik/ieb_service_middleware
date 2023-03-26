"""
"""
from decouple import config, Csv
from ieb_service_middleware.settings.base import *  # NOQA

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())
DEBUG = True
