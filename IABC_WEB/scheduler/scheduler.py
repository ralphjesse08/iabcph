from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from django.utils import timezone
from django_apscheduler.models import DjangoJobExecution
from .updater import schedule_api
import sys

# This is the function you want to schedule - add as many as you want and then register them in the start() function below


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(schedule_api, 'interval', seconds=15)
    #scheduler.add_job(schedule_api, 'interval', days=1)
    register_events(scheduler)
    scheduler.start()
    #print("Scheduler started...", file=sys.stdout)