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

    tables = []

    for i in cursor:
        tables.append(i[0])

    for table in tables:
        mycol = mydb[f"{table}"]
        sql = f"SELECT * FROM {table}"
        columns = [column[0] for column in cursor.description]
        df = pd.read_sql(sql, conn)
        for k in range(0, df.shape[0]):
            diction = {}
            for i in range(0, len(df.loc[k].keys())):
                diction[f"{df.loc[k].keys()[i]}"] = str(df.loc[k].values[i])
            mycol.insert_one(diction)
