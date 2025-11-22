import pandas as pd
import sqlite3

database = 'database.db'
conn = sqlite3.connect(database)
tables = pd.read_sql("""SELECT *
                     FROM sqlite_master
                     WHERE type = 'table'
                     ;""", conn)

print(tables)

df = pd.read_sql("""SELECT * FROM Salesman""", conn)
print(df)

df1 = pd.read_sql("""SELECT * FROM Salesman
                 WHERE city LIKE '%e' ;""", conn)
print(df1)
print(df1.dtypes)
print(df1.columns)

df2 = pd.read_sql("""SELECT SUM(Commission) as total_commission FROM Salesman
                 WHERE Commission > 0.12 ;""", conn)
print(df2)
