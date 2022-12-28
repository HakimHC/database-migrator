import pymongo
import pyodbc
import pandas as pd

connection_string ='Driver={SQL Server};Server=DESKTOP-HNDUMOI\SQLEXPRESS;Database=Almacen;Trusted_Connection=yes;'
db_index = connection_string.find('Database=')
db = connection_string.replace('=', ';')[db_index:].split(';')[1]

conn = pyodbc.connect(connection_string)

cursor = conn.cursor()

cursor.execute(f"SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_CATALOG='{db}'")

tables = []

for i in cursor:
    tables.append(i[0])

for i in tables:
    cursor.execute(f"SELECT * FROM {i}")
    df = pd.DataFrame(cursor.fetchall())
    print(df)