from celery import Celery
from django.conf import settings

app = Celery('loginapp')