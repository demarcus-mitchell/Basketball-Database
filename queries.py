# SCHEMA 
CREATE_ATHLETE_TABLE = """ CREATE TABLE IF NOT EXISTS athlete(
    athlete_id INTEGER PRIMARY KEY AUTOINCREMENT,
    f_name TEXT,
    l_name TEXT,
    position_id INTEGER,
    school_id TEXT,
    height INTEGER,
    weight INTEGER,
    drafted BOOLEAN,
    FOREIGN KEY (position_id) REFERENCES position(position_id),
    FOREIGN KEY (school_id) REFERENCES school(school_id)
    );"""

CREATE_ATHLETE_STATS_TABLE = """ CREATE TABLE IF NOT EXISTS athlete_stats(
    athlete_id INTEGER,
    season_id INTEGER,
    points INTEGER,
    assists INTEGER,
    rebounds INTEGER,
    steals INTEGER,
    blocks INTEGER,
    PRIMARY KEY (athlete_id, season_id)
    );"""


CREATE_POSITION_TABLE = """ CREATE TABLE IF NOT EXISTS position(
    position_id INTEGER PRIMARY KEY,
    position_name TEXT
    );"""

CREATE_SEASON_TABLE = """ CREATE TABLE IF NOT EXISTS season(
    season_id INTEGER PRIMARY KEY,
    season_year DATE
    );"""

CREATE_DRAFT_TABLE = """ CREATE TABLE IF NOT EXISTS draft(
    draft_id TEXT PRIMARY KEY,
    draft_year INTEGER);"""

CREATE_DRAFT_PICK_TABLE = """ CREATE TABLE IF NOT EXISTS draft_pick(
    draft_id INTEGER,
    athlete_id INTEGER,
    draft_round INTEGER,
    round_pick INTEGER,
    overall_selection INTEGER,
    PRIMARY KEY (draft_id, athlete_id)
    );"""

CREATE_SCHOOL_TABLE = """ CREATE TABLE IF NOT EXISTS school(
    school_id TEXT PRIMARY KEY,
    school_name TEXT,
    school_location TEXT,
    school_conference TEXT
    );"""

CREATE_SCHOOL_STATS_TABLE = """ CREATE TABLE IF NOT EXISTS school_stats(
    school_id INTEGER,
    season_id INTEGER,
    assists INTEGER,
    rebounds INTEGER,
    blocks INTEGER,
    steals INTEGER,
    wins INTEGER,
    losses INTEGER,
    PRIMARY KEY (school_id, season_id)
    );"""


# ADD DATA TO TABLES
ADD_ATHLETE = """INSERT INTO athlete (athlete_id, f_name, l_name, position_id, school_id, height, weight, drafted) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 0)"""
ADD_ATHLETE_STATS = """INSERT INTO athlete_stats (athlete_id, season_id, points, assists, rebounds, blocks, steals, games_played) VALUES (?, ?, 0, 0, 0, 0, 0, 0)"""
ADD_POSITION = """INSERT INTO position (position_id, position_name) VALUES (?, ?)"""

ADD_SCHOOL = """INSERT INTO school (school_id, school_name, school_location, school_conference) VALUES (?, ?, ?, ?)"""
ADD_SCHOOL_STATS = """INSERT INTO school_stats (school_id, season_id, points, assists, rebounds, blocks, steals, wins, losses) VALUES (?, ?, 0, 0, 0, 0, 0, 0, 0)"""

ADD_DRAFT = """INSERT INTO draft (draft_id, draft_year) VALUES (?, ?)"""
ADD_DRAFT_PICK = """INSERT INTO draft_pick (draft_id, athlete_id, draft_round, round_pick, overall_selection) VALUES (?, ?, ?, ?, ?)"""

ADD_SEASON = """INSERT INTO season (season_id, season_year) VALUES (?, ?)"""

# VIEW DATA IN TABLES 
#VIEW PLAYER STATS VS TEAMS AND SEASON


#VIEW PLAYER STATS VS Conference AVG

#VIEW PLAYER STATS FOR POSITION
VIEW_POSITION_STATS = """SELECT athlete_stats.* FROM athlete_stats JOIN athlete ON athlete.athlete_id = athlete_stats.athlete_id JOIN position ON athlete.position_id = position.position_id WHERE position.position_id = '?'"""


#VIEW PLAYER STATS RANKED BY STAT CATEGORY


SELECT_ALL_ATHLETE_STATS = "SELECT * FROM athlete_stats;"
#SELECT_POSITION_STATS = "SELECT * FROM athlete-stats WHERE " NEED JOIN WITH position_table SYNTAX
SELECT_ALL_SCHOOLS_STATS = "SELECT * FROM school_stats;"


#CHECK IF PLAYER DRAFTED
CHECK_IF_DRAFTED = "SELECT * FROM athlete WHERE drafted = 'yes';"

#UPDATE PLAYER DRAFT INFO
UPDATE_DRAFT_PICK = "UPDATE draft_pick SET overall_selection = ? FROM draft_pick INNER JOIN athlete ON draft_pick.athlete_id = athlete.athlete_id WHERE athlete.fname = '?' AND athlete.lname = '?';"

#UPDATE PLAYER STATS


