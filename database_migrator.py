import pymongo
import pyodbc
import pandas as pd

def ss_to_mongo(sql_connection_string, mongo_conn, database_name):

    db_index = sql_connection_string.find('Database=')
    db = sql_connection_string.replace('=', ';')[db_index:].split(';')[1]

    conn = pyodbc.connect(sql_connection_string)

    cursor = conn.cursor()

    myclient = pymongo.MongoClient(mongo_conn)

    mydb = myclient[f'{database_name}']

    cursor.execute(f"SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_CATALOG='{db}'")

    tables = [table[0] for table in cursor.fetchall()]

    for table in tables:
        mycol = mydb[f"{table}"]
        sql = f"SELECT * FROM [{table}]"
        df = pd.read_sql(sql, conn)
        df.fillna('Null',inplace=True)
        records = df.to_dict(orient='records')
        if records:
            mycol.insert_many(records)