from flask import Blueprint, request, redirect
from src.models.task_model import task_model

tasks = Blueprint('tasks', __name__, url_prefix='/tasks')
task = task_model()

def get_tasks():
    if 'period' not in request.form:
        return 'Need time period to fetch tasks!'
    if request.form['period'] == 'THIS WEEK':
        return task.get_this_week_tasks()
    if request.form['period'] == 'BACKLOG':
        return task.get_backlog()
    if request.form['period'] == 'FUTURE TASKS':
        return task.get_future_tasks()

@tasks.route('', methods=['POST'])
def create_task():
    data = request.form
    print ("data",data)
    task.create_tasks(data)
    return redirect('/')

@tasks.route('', methods=['GET'])
def delete_task():
    taskid = request.args.get('taskid')
    task.delete_task(taskid)
    return redirect('/')


@tasks.route('/update', methods=['POST'])
def update_task():
    data = request.form
    task.update_task(data)
    return 'Task updated succesfully!', 200


