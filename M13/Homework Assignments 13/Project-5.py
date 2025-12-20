import pandas as pd
import sqlite3

database = 'basketball.sqlite'
conn = sqlite3.connect(database)

tables = pd.read_sql("""SELECT *
                     FROM sqlite_master
                     WHERE type='table' ;""", conn)
print("\nALL TABLES \n")
print(tables)

players = pd.read_sql("""SELECT is_active 
                      FROM Player""", conn)
print("\nALL FROM PLAYERS\n")
print(players)

player_salary = pd.read_sql("""SELECT value
                      FROM Player_Salary""", conn)
print("\nALL FROM PLAYERS SALARY\n")
print(player_salary)

joining_tables = pd.read_sql("""SELECT DISTINCT nameTeam, namePlayer, value
                                          FROM Player_Salary 
                                          AND (SELECT is_active 
                                          FROM Player)
                                         """, conn)
print(joining_tables)