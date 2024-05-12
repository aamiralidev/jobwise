import os 
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djobwise.settings')
# this actually refers to settings.py 
celery = Celery('djobwise')
celery.config_from_object('django.conf:settings', namespace='CELERY')
# this tells celery to load configurations from settings.py and 
# namespace tells that all the celery settings are gonna start
# with this prefix
celery.autodiscover_tasks() 