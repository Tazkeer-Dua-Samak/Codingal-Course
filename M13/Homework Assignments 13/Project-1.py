import pandas as pd
import sqlite3

conn = sqlite3.connect('database_psl.db')

print("\n--- All Teams ---")
teams_df = pd.read_sql("SELECT * FROM teams;", conn)
print(teams_df)

print("\n--- Total matches played by each team ---")
team_stats_df = pd.read_sql("SELECT team_name, total_matches, total_wins, total_losses FROM team_stats;", conn)
print(team_stats_df)

print("\n--- Total trophies won by each team ---")
trophies_df = pd.read_sql("SELECT team_name, trophies_won FROM team_stats ORDER BY trophies_won DESC;", conn)
print(trophies_df)

print("\n--- All matches won by a Lahore Qalandars ---")
matches_won_df = pd.read_sql("""SELECT *
                             FROM matches
                             WHERE winner_team_name = 'Lahore Qalandars';""", conn)
print(matches_won_df)

print("\n--- All Matches won by runs only ---")
runs_wins_df = pd.read_sql("SELECT * FROM matches WHERE win_type = 'runs';", conn)
print(runs_wins_df)

print("\n--- All Matches won by wickets only ---")
wickets_wins_df = pd.read_sql("SELECT * FROM matches WHERE win_type = 'wickets';", conn)
print(wickets_wins_df)

print("\n--- All season champions ---")
season_champs_df = pd.read_sql("SELECT season_year, champion FROM season_awards ORDER BY season_year;", conn)
print(season_champs_df)

print("\n--- All Orange Cap winners ---")
orange_cap_df = pd.read_sql("SELECT season_year, orange_cap FROM season_awards ORDER BY season_year;", conn)
print(orange_cap_df)

print("\n--- All Purple Cap winners ---")
purple_cap_df = pd.read_sql("SELECT season_year, purple_cap FROM season_awards ORDER BY season_year;", conn)
print(purple_cap_df)

print("\n--- Team Performance Stats ---")
team_perf_df = pd.read_sql("SELECT * FROM team_performance ORDER BY win_rate DESC;", conn)
print(team_perf_df)

print("\n--- All Matches with highest margin of win ---")
biggest_win_df = pd.read_sql("SELECT * FROM matches ORDER BY win_margin DESC;", conn)
print(biggest_win_df)

print("\n--- All trophy history of Islamabad United ---")
trophy_history_df = pd.read_sql("""SELECT *
                                FROM trophy_history
                                WHERE team_name = 'Islamabad United';""", conn)
print(trophy_history_df)