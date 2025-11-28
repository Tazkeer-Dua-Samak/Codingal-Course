import sqlite3
import pandas as pd

conn = sqlite3.connect("database_psl.db")


print("--- All matches where Lahore Qalandars won ---")

matches_lq_df = pd.read_sql("""
SELECT *
FROM matches
WHERE winner_team_name = 'Lahore Qalandars';
""", conn)
print(matches_lq_df)


print("--- All teams with names containing 'Karachi' ---")

teams_karachi_df = pd.read_sql("""
SELECT *
FROM teams
WHERE team_name LIKE '%Karachi%';
""", conn)
print(teams_karachi_df)


print("--- Team with minimum number of wins ---")

min_wins_df = pd.read_sql("""
SELECT team_name, total_wins
FROM team_stats
WHERE total_wins = (SELECT MIN(total_wins) FROM team_stats);
""", conn)
print(min_wins_df)


print("--- Team with maximum number of wins ---")

max_wins_df = pd.read_sql("""
SELECT team_name, total_wins
FROM team_stats
WHERE total_wins = (SELECT MAX(total_wins) FROM team_stats);
""", conn)
print(max_wins_df)


print("--- Matches where winner's name contains 'United' ---")

matches_united_df = pd.read_sql("""
SELECT *
FROM matches
WHERE winner_team_name LIKE '%United%';
""", conn)
print(matches_united_df)


print("--- Match with the largest win margin ---")

max_margin_df = pd.read_sql("""
SELECT *
FROM matches
WHERE win_margin = (SELECT MAX(win_margin) FROM matches);
""", conn)
print(max_margin_df)


print("--- Match with the smallest win margin ---")

min_margin_df = pd.read_sql("""
SELECT *
FROM matches
WHERE win_margin = (SELECT MIN(win_margin) FROM matches);
""", conn)
print(min_margin_df)


print("--- All trophies won by teams with 'Sultans' in the name ---")

trophies_sultans_df = pd.read_sql("""
SELECT *
FROM trophies
WHERE winner_team_name LIKE '%Sultans%';
""", conn)
print(trophies_sultans_df)

#For reasons unknown I am informing you that the data shown may not entirely be accurate as I was not the one who researched all this