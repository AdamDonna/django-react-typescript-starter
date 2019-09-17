from celery import Celery


app = Celery("django-react-boilerplace")

app.config_from_object("django.conf:settings")
app.autodiscover_tasks()