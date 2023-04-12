import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

app = Celery('syncer', include=["spotifysyncer.tasks.test_task"])

app.config_from_object('django.conf:settings')
app.worker_prefetch_multiplier = 1
app.task_acks_late = True

app.autodiscover_tasks()