CREATE TABLE IF NOT EXISTS teams (
    team_name TEXT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS matches (
    match_id INTEGER PRIMARY KEY,
    season_year INTEGER,
    team1_name TEXT,
    team2_name TEXT,
    winner_team_name TEXT,
    win_type TEXT,        -- "runs" or "wickets"
    win_margin INTEGER    -- number of runs or wickets
);

CREATE TABLE IF NOT EXISTS trophies (
    trophy_id INTEGER PRIMARY KEY,
    season_year INTEGER,
    winner_team_name TEXT
);

CREATE TABLE IF NOT EXISTS team_stats (
    team_name TEXT PRIMARY KEY,
    total_matches INTEGER,
    total_wins INTEGER,
    total_losses INTEGER,
    trophies_won INTEGER
);

CREATE TABLE IF NOT EXISTS win_methods (
    id INTEGER PRIMARY KEY,
    team_name TEXT,
    runs_wins INTEGER,
    wicket_wins INTEGER
);

CREATE TABLE IF NOT EXISTS trophy_history (
    id INTEGER PRIMARY KEY,
    team_name TEXT,
    trophy_year INTEGER
);

-- INSERT PSL TEAMS

INSERT INTO teams (team_name) VALUES
    ('Islamabad United'),
    ('Karachi Kings'),
    ('Lahore Qalandars'),
    ('Peshawar Zalmi'),
    ('Quetta Gladiators'),
    ('Multan Sultans');

-- TEAM STATS (EXAMPLE DATA)

INSERT INTO team_stats (team_name, total_matches, total_wins, total_losses, trophies_won) VALUES
    ('Islamabad United', 100, 55, 45, 2),
    ('Karachi Kings', 98, 40, 58, 1),
    ('Lahore Qalandars', 95, 42, 53, 2),
    ('Peshawar Zalmi', 102, 48, 54, 1),
    ('Quetta Gladiators', 101, 50, 51, 1),
    ('Multan Sultans', 90, 47, 43, 1);

-- WIN METHODS (EXAMPLE)

INSERT INTO win_methods (id, team_name, runs_wins, wicket_wins) VALUES
    (1, 'Islamabad United', 25, 30),
    (2, 'Karachi Kings', 18, 22),
    (3, 'Lahore Qalandars', 20, 22),
    (4, 'Peshawar Zalmi', 23, 25),
    (5, 'Quetta Gladiators', 26, 24),
    (6, 'Multan Sultans', 22, 25);

-- TROPHY HISTORY

INSERT INTO trophy_history (id, team_name, trophy_year) VALUES
    (1, 'Islamabad United', 2016),
    (2, 'Islamabad United', 2018),
    (3, 'Lahore Qalandars', 2022),
    (4, 'Lahore Qalandars', 2023),
    (5, 'Peshawar Zalmi', 2017),
    (6, 'Quetta Gladiators', 2019),
    (7, 'Multan Sultans', 2021);

-- TROPHIES (CURRENT SEASON WINNERS)

INSERT INTO trophies (trophy_id, season_year, winner_team_name) VALUES
    (1, 2016, 'Islamabad United'),
    (2, 2019, 'Quetta Gladiators'),
    (3, 2020, 'Karachi Kings'),
    (4, 2022, 'Lahore Qalandars'),
    (5, 2023, 'Lahore Qalandars'),
    (6, 2021, 'Multan Sultans');

-- MATCHES (SIMPLE EXAMPLE DATA)

INSERT INTO matches (match_id, season_year, team1_name, team2_name, winner_team_name, win_type, win_margin) VALUES
    (1, 2023, 'Islamabad United', 'Lahore Qalandars', 'Islamabad United', 'runs', 15),
    (2, 2023, 'Karachi Kings', 'Peshawar Zalmi', 'Peshawar Zalmi', 'wickets', 6),
    (3, 2023, 'Multan Sultans', 'Quetta Gladiators', 'Multan Sultans', 'runs', 30),
    (4, 2024, 'Lahore Qalandars', 'Peshawar Zalmi', 'Lahore Qalandars', 'wickets', 4);

-- SEASON AWARDS (REAL DATA)

CREATE TABLE IF NOT EXISTS season_awards (
    season_year INTEGER PRIMARY KEY,
    champion TEXT,
    runner_up TEXT,
    orange_cap TEXT,
    purple_cap TEXT,
    best_economy TEXT,
    emerging_player TEXT,
    best_fielder TEXT
);

INSERT INTO season_awards (season_year, champion, runner_up, orange_cap, purple_cap, best_economy, emerging_player, best_fielder) VALUES
    (2023, 'Lahore Qalandars', 'Multan Sultans', 'Mohammad Rizwan', 'Abbas Afridi', 'Ihsanullah', 'Abbas Afridi', 'Kieron Pollard'),
    (2022, 'Lahore Qalandars', 'Peshawar Zalmi', 'Fakhar Zaman', 'Shane Afridi', 'Zaman Khan', 'Mohammad Haris', 'Kieron Pollard'),
    (2021, 'Multan Sultans', 'Peshawar Zalmi', 'Babar Azam', 'Shahnawaz Dahani', 'Imran Tahir', 'Shahnawaz Dahani', 'David Miller');

-- TEAM PERFORMANCE 

CREATE TABLE IF NOT EXISTS team_performance (
    team_name TEXT PRIMARY KEY,
    win_rate REAL,
    titles INTEGER,
    highest_total TEXT,
    lowest_total TEXT,
    biggest_win TEXT,
    longest_win_streak INTEGER
);

INSERT INTO team_performance (team_name, win_rate, titles, highest_total, lowest_total, biggest_win, longest_win_streak) VALUES
    ('Islamabad United', 55.09, 2, '247/2', '82', '78 runs', 6),
    ('Lahore Qalandars', 50.00, 2, '226/5', '59', '67 runs', 5),
    ('Peshawar Zalmi', 50.52, 1, '244/6', '73', '55 runs', 6),
    ('Multan Sultans', 54.28, 1, '245/3', '80', '9 wickets', 5),
    ('Quetta Gladiators', 49.42, 1, '203/5', '90', '8 wickets', 4),
    ('Karachi Kings', 45.45, 1, '201/4', '86', '10 wickets', 4);


SELECT * FROM teams;
SELECT * FROM team_stats;
SELECT * FROM matches;
SELECT * FROM team_performance;
SELECT * FROM season_awards;
SELECT * FROM trophies;
SELECT * FROM trophy_history;
SELECT * FROM win_methods;

SELECT team_name, total_matches, total_wins, total_losses
FROM team_stats;

SELECT team_name, trophies_won
FROM team_stats
ORDER BY trophies_won DESC;

SELECT *
FROM matches
WHERE winner_team_name = 'Lahore Qalandars';

SELECT *
FROM matches
WHERE win_type = 'runs';

SELECT *
FROM matches
WHERE win_type = 'wickets';

SELECT season_year, champion
FROM season_awards
ORDER BY season_year;

SELECT season_year, orange_cap
FROM season_awards
ORDER BY season_year;

SELECT season_year, purple_cap
FROM season_awards
ORDER BY season_year;

SELECT *
FROM team_performance
ORDER BY win_rate DESC;

SELECT *
FROM matches
ORDER BY win_margin DESC;

SELECT *
FROM trophy_history
WHERE team_name = 'Islamabad United';
