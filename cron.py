import time
import atexit
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import src.models.task_model as task_model
import src.models.category_model as category_model
from src.controller.task_controller import tasks
import smtplib, ssl

email = "simpliischeduling"
password = "Ihaveapassword12!"
port = 465
smtp_server = "smtp.gmail.com"
context = ssl.create_default_context()



def print_date_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))

def send_daily_alerts():
    todays_tasks = task_model.task_model.get_todays_tasks()

    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
    
    except Exception as e:
        print(e)

    for task in todays_tasks:
        userID = task.get("UserID")
        receiver_email = task_model.task_model.get_user_by_id(userID).get("EmailID")
        message = """\
        Subject: Daily Simplii Reminder

        Dear {},
        
        This is an email reminder for the task {}, taking place on {}.
        
        Regards,
        Simplii
        
        This message was sent automatically, please do not reply.""".format(userID, task.get("Taskname"), task.get("Startdate"))
        server.sendmail(email, receiver_email, message)
    server.quit()





scheduler = BackgroundScheduler()
scheduler.add_job(func=send_daily_alerts, trigger="interval", hours=24)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

