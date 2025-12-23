import pandas as pd
import sqlite3

database = 'basketball.sqlite'
conn = sqlite3.connect(database)

tables = pd.read_sql("""
                     SELECT *
                     FROM sqlite_master
                     WHERE type = 'table';
                     """, conn)
print(tables)

player = pd.read_sql("""
                     SELECT *
                     FROM Player;
                     """, conn)
print(player)

player_salary = pd.read_sql("""
                            SELECT *
                            FROM Player_Salary;
                            """, conn)
print(player_salary)

joined_salary = pd.read_sql("""
                            SELECT ps.nameTeam,
                                   ps.namePlayer,
                                   ps.value,
                                   p.is_active
                            FROM Player_Salary ps
                            INNER JOIN Player p
                            ON ps.namePlayer = p.full_name
                            GROUP BY ps.nameTeam;
                            """, conn)
print(joined_salary)

