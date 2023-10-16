from src.error_handler.error import handle_err
from flask import Flask, render_template, redirect, session, request
from flask_apscheduler import APScheduler, scheduler
from apscheduler.schedulers.background import BackgroundScheduler
import src.models.task_model as task_model
import src.models.category_model as category_model
from src.controller.task_controller import tasks
from src.login.login import login
import notif_system as notification_system

app = Flask(__name__)
app.register_blueprint(handle_err)
app.register_blueprint(tasks)
app.register_blueprint(login)
app.config.from_object(notification_system.Config())
app.config['SECRET_KEY'] = 'SECRET_KEY'

@app.route("/login")
def load_login():
    """This function renders the login page."""
    return render_template("login.html")

@app.route("/")
def homePage():
    currUserName = None
    if "username" in session.keys():
        currUserName = session["username"]
    if not currUserName:
        return redirect("/login")
    this_week_tasks = task_model.task_model.get_this_week_tasks(currUserName)
    backlog_tasks = task_model.task_model.get_backlog(currUserName)
    future_tasks = task_model.task_model.get_future_tasks(currUserName)
    categories = category_model.category_model.get_category()
    """This function renders the home page."""
    return render_template("home.html", this_week_tasks=this_week_tasks,
    backlog_tasks=backlog_tasks, future_tasks=future_tasks, categories= categories)

@app.route("/edit_task")
def edit_task():
    """This function renders the edit task page."""
    task_id = request.args.get('task_id')
    return render_template("edit_task.html",task_id = task_id)

@app.route("/view_all_tasks")
def view_all_tasks():
    all_tasks = task_model.task_model.get_all_taks()
    """This function renders the edit task page."""
    return render_template("view_all_tasks.html", all_tasks=all_tasks)

@app.route("/user_details")
def user_details():
    """This function renders the edit task page."""
    return render_template("view_user_details.html")


if __name__ == "__main__":
    #notification_system.scheduler.init_app(app)
    print("Hello")
    #notification_system.scheduler.add_job(func=notification_system.send_test_alerts, trigger="interval", minutes=1)
    #notification_system.scheduler.start()
    app.run(debug=True)

