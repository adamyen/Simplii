
import pandas as pd
from src.models.sql_helper import sql_helper

con = sql_helper()
class category_model:
    def create_category(self, data):
        columns = ''
        values = ''
        for key, value in data.items():
            columns += str(key)+', '
            values += "'"+str(value)+"', "

        query = "INSERT INTO  ("+columns[:-2]+" ) VALUES (" + values[:-2]+" );"
        con.run_query(query)
        return
    
    def get_category():
        query = "SELECT Category_ID, Category_name FROM Categories;"
        result = con.run_query(query)
        result = pd.DataFrame(list(result))
        return result.to_dict('records')

    def update_category(self, data):
        values = ''
        for key, value in data.items():
            values += str(key)+"= '"+str(value)+"', "
        query = "UPDATE tasks SET "+values[:-2]+";"
        con.run_query(query)
        return



