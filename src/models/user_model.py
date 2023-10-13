
import pandas as pd
from src.models.sql_helper import sql_helper
import uuid

con = sql_helper()
class user_model:
    def create_user(self, data):
        print(data)
        userID = 1034
        columns = 'UserID, '
        values = f'{userID}, '
        for key, value in data.items():
            columns += str(key)+', '
            values += "'"+str(value)+"', "

        
        query = "INSERT INTO User ("+columns[:-2]+" ) VALUES (" + values[:-2]+" );"
        print(query)
        try:
            x = con.run_query(query)
            print("From model ", x)
            return True
        except Exception as e:
            print(e)
            return False