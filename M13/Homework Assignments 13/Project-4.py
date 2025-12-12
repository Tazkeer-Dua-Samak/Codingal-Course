import sqlite3
import pandas as pd

database = 'basketball.sqlite'
conn = sqlite3.connect(database)

print("Opened database successfully!")

tables = pd.read_sql("""SELECT * 
                     FROM sqlite_master
                     WHERE type = 'table';""", conn)

print("All tables in the database: ")
print(tables)

draft = pd.read_sql(
    """
    SELECT *
    FROM Draft
    WHERE nameOrganizationFrom = '';
    """,
    conn
)
print(draft)

EarliestFoundTeams = pd.read_sql("""
    SELECT *
    FROM Team
    ORDER BY id ASC
    LIMIT 5;
""", conn)
print(EarliestFoundTeams)

LatestFoundTeams = pd.read_sql("""
    SELECT *
    FROM Team
    ORDER BY id DESC
    LIMIT 5;
""", conn)
print(LatestFoundTeams)
