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
    games_played INTEGER,
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


# Add Seasons, Positions, Schools, Drafts, Athletes
ADD_SEASON = """INSERT INTO season (season_id, season_year) VALUES (?, ?)"""
ADD_POSITION = """INSERT INTO position (position_id, position_name) VALUES (?, ?)"""
ADD_SCHOOL = """INSERT INTO school (school_id, school_name, school_location, school_conference) VALUES (?, ?, ?, ?)"""
ADD_DRAFT = """INSERT INTO draft (draft_id, draft_year) VALUES (?, ?)"""
ADD_ATHLETE = """INSERT INTO athlete (athlete_id, f_name, l_name, position_id, school_id, height, weight, drafted) VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)"""


# |------------- REQUIRED QUERIES -------------|
#Insert new players, teams, and seasons --- DONE

#Add new draft data for a player who already exists in your data.

#Check if player participated in the draft
CHECK_IF_DRAFTED = """SELECT f_name, l_name, school_id FROM athlete WHERE f_name = ? AND l_name = ? AND drafted = Y"""
#Remove players and teams

#Search for players by name, school, or class rank
FIND_ATHLETE_ID = """SELECT athlete_id, f_name, last_name, school_id FROM athlete WHERE f_name = ? AND l_name = ? AND school_id = ?"""
#Update player statistics

#View player statistics compared to team statistics.
#View player statistics compared to league average.
#View player statistics for specific positions
#View players ranked by a specific statistic.



# Update Stats, Draft Info
UPDATE_DRAFT_PICK = "UPDATE draft_pick SET overall_selection = ? FROM draft_pick INNER JOIN athlete ON draft_pick.athlete_id = athlete.athlete_id WHERE athlete.fname = '?' AND athlete.lname = '?';"
UPDATE_SCHOOL_STATS = """INSERT INTO school_stats (school_id, season_id, points, assists, rebounds, blocks, steals, wins, losses) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""

ADD_ATHLETE_STATS_BY_NAME = """INSERT INTO athlete_stats (athlete_id, season_id, points, assists, rebounds, blocks, steals, games_played) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""

UPDATE_ATHLETE_STATS_BY_NAME = """UPDATE athlete_stats 
SET points = ?, assists = ?, rebounds = ?, blocks = ?, steals = ?, games_played = ?
WHERE athlete_id = (
    SELECT athlete_id FROM athlete
    WHERE f_name = ? AND l_name = ? AND school_id = ?
    )
    AND season_id = ?;
    """
ADD_DRAFT_PICK = """INSERT INTO draft_pick (draft_id, athlete_id, draft_round, round_pick, overall_selection) VALUES (?, ?, ?, ?, ?)"""


# VIEW Athlete DATA
SELECT_ALL_ATHLETE_STATS = "SELECT * FROM athlete_stats;" #VIEW ALL PLYER STATS


#VIEW PLAYER STATS VS Conference AVG

#VIEW PLAYER STATS FOR POSITION
VIEW_POSITION_STATS = """SELECT FROM athlete_stats JOIN athlete ON athlete.athlete_id = athlete_stats.athlete_id JOIN position ON athlete.position_id = position.position_id WHERE position.position_id = '?'"""


#VIEW PLAYER STATS RANKED BY STAT CATEGORY



#SELECT_POSITION_STATS = "SELECT * FROM athlete-stats WHERE " NEED JOIN WITH position_table SYNTAX
SELECT_ALL_SCHOOLS_STATS = "SELECT * FROM school_stats;"







