import pandas as pd
import sqlite3

database = 'basketball.sqlite'
conn = sqlite3.connect(database)

tables = pd.read_sql("""SELECT *
                        FROM sqlite_master
                        WHERE type='table';""", conn)
print(tables)

draft = pd.read_sql("""SELECT * FROM Draft""", conn)
print(draft)

distinct_draft_years = pd.read_sql("""SELECT DISTINCT yearDraft
                                      FROM Draft
                                      ORDER BY yearDraft;""", conn)
print("Distinct draft years:")
print(distinct_draft_years)

top_picks = pd.read_sql("""SELECT namePlayer, nameTeam, numberPickOverall
                           FROM Draft
                           ORDER BY numberPickOverall
                           LIMIT 10;""", conn)
print("Top 10 overall draft picks:")
print(top_picks)

drafts_per_year = pd.read_sql("""SELECT yearDraft, COUNT(*) AS total_players_drafted
                                 FROM Draft
                                 GROUP BY yearDraft
                                 ORDER BY yearDraft;""", conn)
print("Total players drafted per year:")
print(drafts_per_year)

avg_pick_by_round = pd.read_sql("""SELECT numberRound, 
                                          AVG(numberPickOverall) AS avg_overall_pick
                                   FROM Draft
                                   GROUP BY numberRound
                                   ORDER BY numberRound;""", conn)
print("Average overall pick by round:")
print(avg_pick_by_round)

players_by_team = pd.read_sql("""SELECT nameTeam, COUNT(*) AS total_players
                                 FROM Draft
                                 GROUP BY nameTeam
                                 ORDER BY total_players DESC;""", conn)
print("Total players drafted by each team:")
print(players_by_team)
