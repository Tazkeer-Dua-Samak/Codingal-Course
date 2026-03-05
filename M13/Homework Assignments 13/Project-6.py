import pandas as pd
import sqlite3

database = 'basketball.sqlite'
conn = sqlite3.connect(database)

tables = pd.read_sql("""SELECT *
                     FROM sqlite_master
                     WHERE type='table' ;""", conn)
print(tables)

team = pd.read_sql("""SELECT * FROM Team""", conn)
print("Team", team)

team_attributes = pd.read_sql("""SELECT * FROM Team_Attributes""", conn)
print("Team_Attributes", team_attributes)

ny_teams = pd.read_sql("""SELECT ta.*
                        FROM Team_Attributes AS ta
                        WHERE ta.ID IN
                        (SELECT id
                         FROM Team
                         WHERE state = 'New York')""", conn)
print(ny_teams)
print(team.columns)
print(team_attributes.columns)