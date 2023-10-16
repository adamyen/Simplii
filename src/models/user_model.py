
import pandas as pd
from src.models.sql_helper import sql_helper
import uuid

con = sql_helper()
class user_model:
    def create_user(self, data):
        userID = uuid.uuid4()
        columns = 'UserId, '
        values = f'\'{userID}\', '
        for key, value in data.items():
            columns += str(key)+', '
            values += "'"+str(value)+"', "

        
        query = "INSERT INTO User ("+columns[:-2]+" ) VALUES (" + values[:-2]+" );"
        
        try:
            con.run_query(query)
            return True
        except Exception as e:
            print(e)
            return False
    
    def login(self, data):
        username = data['username']
        password = data['password']
        query = f"SELECT Password FROM User WHERE EmailId = \'{username}\'"

        x = con.run_query(query)

        if x:
            check = x[0][0]
            if password == check:
                return True
        return False

    def get_loggedIn_User(self, username):
        query = f"SELECT UserId, EmailId, FullName FROM User WHERE EmailId = \'{username}\'"
        x = con.run_query(query)
        return x[0]

