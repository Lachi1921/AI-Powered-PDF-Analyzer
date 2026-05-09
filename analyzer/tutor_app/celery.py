import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutor_app.settings')

celery_app = Celery('tutor_app')

celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()