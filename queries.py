"""
Schema:

athlete
    athlete_id INTEGER PK AUTOINCREMENT
    f_name TEXT
    l_name TEXT
    position_id INTEGER  → position(position_id)
    school_id TEXT       → school(school_id)
    height INTEGER
    weight INTEGER
    drafted BOOLEAN

athlete_stats
    athlete_id INTEGER   → athlete(athlete_id)
    season_id INTEGER    → season(season_id)
    points, assists, rebounds, steals, blocks, games_played INTEGER
    PK (athlete_id, season_id)

position
    position_id INTEGER PK
    position_name TEXT

season
    season_id INTEGER PK
    season_year INTEGER

draft
    draft_id INTEGER PK
    draft_year INTEGER

draft_pick
    draft_id TEXT        → draft(draft_id)
    athlete_id INTEGER   → athlete(athlete_id)
    draft_round, round_pick, overall_selection INTEGER
    PK (draft_id, athlete_id)

school
    school_id TEXT PK
    school_name TEXT
    school_location TEXT
    school_conference TEXT

school_stats
    school_id TEXT       → school(school_id)
    season_id INTEGER    → season(season_id)
    points, assists, rebounds, blocks, steals, wins, losses INTEGER
    PK (school_id, season_id)
"""


# Schema
CREATE_POSITION_TABLE = """
CREATE TABLE IF NOT EXISTS position (
    position_id   INTEGER PRIMARY KEY,
    position_name TEXT NOT NULL
);"""

CREATE_SCHOOL_TABLE = """
CREATE TABLE IF NOT EXISTS school (
    school_id         TEXT PRIMARY KEY,
    school_name       TEXT NOT NULL,
    school_location   TEXT,
    school_conference TEXT
);"""

CREATE_SEASON_TABLE = """
CREATE TABLE IF NOT EXISTS season (
    season_id   INTEGER PRIMARY KEY,
    season_year INTEGER
);"""

CREATE_DRAFT_TABLE = """
CREATE TABLE IF NOT EXISTS draft (
    draft_id   INTEGER PRIMARY KEY,
    draft_year INTEGER NOT NULL
);"""

CREATE_ATHLETE_TABLE = """
CREATE TABLE IF NOT EXISTS athlete (
    athlete_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    f_name      TEXT,
    l_name      TEXT,
    position_id INTEGER,
    school_id   TEXT,
    height      INTEGER,
    weight      INTEGER,
    drafted     BOOLEAN,
    FOREIGN KEY (position_id) REFERENCES position(position_id)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (school_id) REFERENCES school(school_id)
        ON DELETE RESTRICT ON UPDATE CASCADE
);"""

CREATE_ATHLETE_STATS_TABLE = """
CREATE TABLE IF NOT EXISTS athlete_stats (
    athlete_id   INTEGER NOT NULL,
    season_id    INTEGER NOT NULL,
    points       INTEGER,
    assists      INTEGER,
    rebounds     INTEGER,
    steals       INTEGER,
    blocks       INTEGER,
    games_played INTEGER,
    PRIMARY KEY (athlete_id, season_id),
    FOREIGN KEY (athlete_id) REFERENCES athlete(athlete_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (season_id) REFERENCES season(season_id)
        ON DELETE RESTRICT ON UPDATE CASCADE
);"""

CREATE_SCHOOL_STATS_TABLE = """
CREATE TABLE IF NOT EXISTS school_stats (
    school_id TEXT    NOT NULL,
    season_id INTEGER NOT NULL,
    points    INTEGER,
    assists   INTEGER,
    rebounds  INTEGER,
    blocks    INTEGER,
    steals    INTEGER,
    wins      INTEGER,
    losses    INTEGER,
    PRIMARY KEY (school_id, season_id),
    FOREIGN KEY (school_id) REFERENCES school(school_id)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (season_id) REFERENCES season(season_id)
        ON DELETE RESTRICT ON UPDATE CASCADE
);"""

CREATE_DRAFT_PICK_TABLE = """
CREATE TABLE IF NOT EXISTS draft_pick (
    draft_id          INTEGER NOT NULL,
    athlete_id        INTEGER NOT NULL,
    draft_round       INTEGER,
    round_pick        INTEGER,
    overall_selection INTEGER,
    PRIMARY KEY (draft_id, athlete_id),
    FOREIGN KEY (draft_id) REFERENCES draft(draft_id)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (athlete_id) REFERENCES athlete(athlete_id)
        ON DELETE RESTRICT ON UPDATE CASCADE
);"""


# Insert
ADD_POSITION = "INSERT INTO position (position_id, position_name) VALUES (?, ?);"
ADD_SCHOOL = """INSERT INTO school (school_id, school_name, school_location, school_conference)
                VALUES (?, ?, ?, ?);"""
ADD_SEASON = "INSERT INTO season (season_id, season_year) VALUES (?, ?);"
ADD_DRAFT = "INSERT INTO draft (draft_id, draft_year) VALUES (?, ?);"
ADD_ATHLETE = """INSERT INTO athlete (f_name, l_name, position_id, school_id, height, weight, drafted)
                 VALUES (?, ?, ?, ?, ?, ?, ?);"""
ADD_ATHLETE_STATS = """INSERT INTO athlete_stats
    (athlete_id, season_id, points, assists, rebounds, steals, blocks, games_played)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""
ADD_ATHLETE_STATS_BY_NAME = """
INSERT INTO athlete_stats
    (athlete_id, season_id, points, assists, rebounds, steals, blocks, games_played)
SELECT athlete.athlete_id, ?, ?, ?, ?, ?, ?, ?
FROM athlete
WHERE athlete.f_name = ? AND athlete.l_name = ? AND athlete.school_id = ?;
"""
ADD_SCHOOL_STATS = """INSERT INTO school_stats
    (school_id, season_id, points, assists, rebounds, blocks, steals, wins, losses)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"""
ADD_DRAFT_PICK = """INSERT INTO draft_pick
    (draft_id, athlete_id, draft_round, round_pick, overall_selection)
    VALUES (?, ?, ?, ?, ?);"""


# Update
UPDATE_ATHLETE_STATS_BY_NAME = """
UPDATE athlete_stats
SET points = ?, assists = ?, rebounds = ?, steals = ?, blocks = ?, games_played = ?
WHERE athlete_id = (
    SELECT athlete.athlete_id FROM athlete
    WHERE athlete.f_name = ? AND athlete.l_name = ? AND athlete.school_id = ?
) AND season_id = ?;
"""

UPDATE_SCHOOL_STATS = """
UPDATE school_stats
SET points = ?, assists = ?, rebounds = ?, blocks = ?, steals = ?, wins = ?, losses = ?
WHERE school_id = ? AND season_id = ?;"""


# Select / View
VIEW_POSITION_STATS = """
SELECT 
    athlete.athlete_id,
    athlete.f_name,
    athlete.l_name,
    position.position_name,
    athlete_stats.season_id,
    athlete_stats.points,
    athlete_stats.assists,
    athlete_stats.rebounds,
    athlete_stats.steals,
    athlete_stats.blocks,
    athlete_stats.games_played
FROM athlete
JOIN athlete_stats ON athlete.athlete_id = athlete_stats.athlete_id
JOIN position ON athlete.position_id = position.position_id
WHERE position.position_id = ?
ORDER BY athlete_stats.season_id, athlete.l_name, athlete.f_name;
"""

VIEW_PLAYERS_RANKED_BY_STAT = """
SELECT 
    athlete.athlete_id,
    athlete.f_name,
    athlete.l_name,
    school.school_name,
    SUM(athlete_stats.{stat_column}) AS total_stat
FROM athlete
JOIN athlete_stats ON athlete.athlete_id = athlete_stats.athlete_id
JOIN school ON athlete.school_id = school.school_id
GROUP BY athlete.athlete_id, athlete.f_name, athlete.l_name, school.school_name
ORDER BY total_stat DESC;
"""


VIEW_CONFERENCE_AVERAGES = """
SELECT 
    school.school_conference,
    AVG(school_stats.points)   AS avg_points,
    AVG(school_stats.assists)  AS avg_assists,
    AVG(school_stats.rebounds) AS avg_rebounds,
    AVG(school_stats.steals)   AS avg_steals,
    AVG(school_stats.blocks)   AS avg_blocks
FROM school
JOIN school_stats ON school.school_id = school_stats.school_id
WHERE school.school_conference = (
    SELECT school.school_conference
    FROM athlete
    JOIN school ON athlete.school_id = school.school_id
    WHERE athlete.f_name = ? AND athlete.l_name = ?
)
GROUP BY school.school_conference;
"""

VIEW_ATHLETE_STATS = """
SELECT 
    athlete.athlete_id,
    athlete.f_name,
    athlete.l_name,
    athlete_stats.season_id,
    athlete_stats.points,
    athlete_stats.assists,
    athlete_stats.rebounds,
    athlete_stats.steals,
    athlete_stats.blocks,
    athlete_stats.games_played
FROM athlete
JOIN athlete_stats ON athlete.athlete_id = athlete_stats.athlete_id
WHERE athlete.f_name = ? AND athlete.l_name = ?
ORDER BY athlete_stats.season_id;
"""

VIEW_ATHLETE_AVERAGES = """
SELECT 
    athlete.f_name,
    athlete.l_name,
    AVG(athlete_stats.points)        AS avg_points,
    AVG(athlete_stats.assists)       AS avg_assists,
    AVG(athlete_stats.rebounds)      AS avg_rebounds,
    AVG(athlete_stats.steals)        AS avg_steals,
    AVG(athlete_stats.blocks)        AS avg_blocks,
    AVG(athlete_stats.games_played)  AS avg_games
FROM athlete
JOIN athlete_stats ON athlete.athlete_id = athlete_stats.athlete_id
WHERE athlete.f_name = ? AND athlete.l_name = ?
GROUP BY athlete.f_name, athlete.l_name;
"""

VIEW_ALL_ATHLETES = """
SELECT 
    athlete.athlete_id,
    athlete.f_name,
    athlete.l_name,
    position.position_name,
    school.school_name,
    athlete.height,
    athlete.weight,
    athlete.drafted
FROM athlete 
LEFT JOIN position ON athlete.position_id = position.position_id
LEFT JOIN school ON athlete.school_id = school.school_id
ORDER BY athlete.l_name, athlete.f_name;"""

# Checks
CHECK_ATHLETE_EXISTS = "SELECT 1 FROM athlete WHERE f_name = ? AND l_name = ? AND school_id = ?;"
CHECK_SCHOOL_EXISTS = "SELECT 1 FROM school WHERE school_id = ?;"
CHECK_SEASON_EXISTS = "SELECT 1 FROM season WHERE season_id = ?;"


# Delete
DELETE_ATHLETE = "DELETE FROM athlete WHERE athlete_id = ?;"
DELETE_ATHLETE_BY_NAME = "DELETE FROM athlete WHERE f_name = ? AND l_name = ? AND school_id = ?;"