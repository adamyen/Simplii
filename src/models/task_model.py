import pandas as pd
from src.models.sql_helper import sql_helper
from datetime import datetime, timedelta, date
import uuid
from flask import flash

con = sql_helper()

class task_model:
    def __init__(self):
        pass

    def get_all_taks():
        query = "SELECT *, Categories.Category_name, DATE(Startdate), DATE(Duedate) FROM Tasks JOIN Categories ON Tasks.Category= Categories.Category_ID"
        print(query)
        result = con.run_query(query)
        result = pd.DataFrame(list(result))
        return result.to_dict('records')
    
    def get_this_week_tasks(currUserName, current_date=None):
        if(current_date == None):
            current_date = date.today()
        dt = current_date
        start_date = dt - timedelta(days=dt.weekday())
        end_date = start_date + timedelta(days=6)
        query = "SELECT *, Categories.Category_name FROM Tasks JOIN Categories ON Tasks.Category= Categories.Category_ID WHERE (Startdate <='"+str(end_date)+"' AND Duedate >='"+str(start_date)+'\' AND UserID = '+"\'"+currUserName+'\')'
        result = con.run_query(query)
        result = pd.DataFrame(list(result))
        return result.to_dict('records')

    def get_todays_tasks(currUserName, current_date=None):
        if(current_date == None):
            current_date = date.today()
        dt = current_date
        start_date = dt - timedelta(days=dt.weekday())
        end_date = start_date + timedelta(hours=23)
        query = "SELECT *, Categories.Category_name FROM Tasks JOIN Categories ON Tasks.Category= Categories.Category_ID WHERE (Startdate <='"+str(end_date)+"' AND Duedate >='"+str(start_date)+'\' AND UserID = '+"\'"+currUserName+'\')'
        result = con.run_query(query)
        result = pd.DataFrame(list(result))
        return result.to_dict('records')

    def get_backlog(currUserName, current_date=None):
        if(current_date == None):
            current_date = date.today()
        dt = current_date
        start_date = dt - timedelta(days=dt.weekday())
        query = "SELECT  *, Categories.Category_name, DATE(Duedate) FROM Tasks JOIN Categories ON Tasks.Category= Categories.Category_ID WHERE Duedate <='"+str(start_date)+'\' and status <> "Done" AND UserID = '+"\'"+currUserName+"\'"
        result = con.run_query(query)
        result = pd.DataFrame(list(result))
        return result.to_dict('records')

    def get_future_tasks(currUserName, current_date=None):
        if(current_date == None):
            current_date = date.today()
        dt = current_date
        start_date = dt - timedelta(days=dt.weekday())
        end_date = start_date + timedelta(days=6)
        query = "SELECT  *, Categories.Category_name, DATE(Duedate) FROM Tasks JOIN Categories ON Tasks.Category= Categories.Category_ID WHERE Startdate >='"+str(end_date)+"' AND UserID = \'"+currUserName+"\'"
        result = con.run_query(query)
        result = pd.DataFrame(list(result))
        return result.to_dict('records')

    def create_tasks(self, data):
        columns = 'TaskID, '
        values = f'\'{uuid.uuid4()}\', '
        for key, value in data.items():
            columns += str(key)+', '
            values += "'"+str(value)+"', "

        query = "INSERT INTO Tasks ("+columns[:-2]+" ) VALUES (" + values[:-2]+" );"
        print(query)
        con.run_query(query)
        return

    def delete_task(self, taskid):
        query = "DELETE FROM tasks WHERE Taskid ="+ taskid
        con.run_query(query)

    def get_task_by_id(self, taskid):
        query = "SELECT * FROM tasks WHERE Taskid =" + taskid
        result = con.run_query(query)
        return result.to_dict('records')

    def get_user_by_id(self, userid):
        query = "SELECT * FROM user WHERE Userid =" + userid
        result = con.run_query(query)
        return result.to_dict('records')

    def update_task(self, task_id, data):
        values = ''
        for key, value in data.items():
            values += f"{key} = '{value}', "
        query = f"UPDATE Tasks SET {values[:-2]} WHERE TaskID = '{task_id}';"
        con.run_query(query)
        return

