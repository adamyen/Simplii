import time
import atexit
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import src.models.task_model as task_model
import src.models.category_model as category_model
from src.controller.task_controller import tasks

email = "simpliischeduling"
password = "Ihaveapassword12!"

def print_date_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))

def send_daily_alerts():
    todays_tasks = task_model.task_model.get_todays_tasks()
    for task in todays_tasks:
        


scheduler = BackgroundScheduler()
scheduler.add_job(func=send_daily_alerts, trigger="interval", hours=24)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

