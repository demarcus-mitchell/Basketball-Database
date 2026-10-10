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
    FOREIGN KEY (position_id) REFERENCES position(position_id)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (school_id)   REFERENCES school(school_id)
        ON DELETE RESTRICT ON UPDATE CASCADE
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
    FOREIGN KEY (athlete_id) REFERENCES athlete(athlete_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (season_id)  REFERENCES season(season_id)
        ON DELETE RESTRICT ON UPDATE CASCADE
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
    draft_id INTEGER PRIMARY KEY,
    draft_year INTEGER);"""

CREATE_DRAFT_PICK_TABLE = """ CREATE TABLE IF NOT EXISTS draft_pick(
    draft_id INTEGER,
    athlete_id INTEGER,
    draft_round INTEGER,
    round_pick INTEGER,
    overall_selection INTEGER,
    PRIMARY KEY (draft_id, athlete_id)
    FOREIGN KEY (draft_id)   REFERENCES draft(draft_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (athlete_id) REFERENCES athlete(athlete_id)
        ON DELETE CASCADE ON UPDATE CASCADE
    );"""

CREATE_SCHOOL_TABLE = """ CREATE TABLE IF NOT EXISTS school(
    school_id TEXT PRIMARY KEY,
    school_name TEXT,
    school_location TEXT,
    school_conference TEXT
    );"""

CREATE_SCHOOL_STATS_TABLE = """ CREATE TABLE IF NOT EXISTS school_stats(
    school_id TEXT,
    season_id INTEGER,
    points INTEGER,
    assists INTEGER,
    rebounds INTEGER,
    blocks INTEGER,
    steals INTEGER,
    wins INTEGER,
    losses INTEGER,
    PRIMARY KEY (school_id, season_id)
    FOREIGN KEY (school_id) REFERENCES school(school_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (season_id) REFERENCES season(season_id)
        ON DELETE RESTRICT ON UPDATE CASCADE
    );"""

# INSERT Seasons, Positions, Schools, Drafts, Athletes, Athlete Stats, School Stats
ADD_SEASON = """INSERT INTO season (season_id, season_year) VALUES (?, ?);"""

ADD_POSITION = """INSERT INTO position (position_id, position_name) VALUES (?, ?);"""

ADD_SCHOOL = """INSERT INTO school (school_id, school_name, school_location, school_conference) VALUES (?, ?, ?, ?);"""

ADD_SCHOOL_STATS = """INSERT INTO school_stats (school_id, season_id, points, assists, rebounds, blocks, steals, wins, losses) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"""

ADD_DRAFT = """INSERT INTO draft (draft_id, draft_year) VALUES (?, ?);"""

ADD_DRAFT_PICK = """INSERT INTO draft_pick (draft_id, athlete_id, draft_round, round_pick, overall_selection) VALUES (?, ?, ?, ?, ?);"""

ADD_ATHLETE = """INSERT INTO athlete (f_name, l_name, position_id, school_id, height, weight, drafted) VALUES (?, ?, ?, ?, ?, ?, ?);"""

ADD_ATHLETE_STATS = """INSERT INTO athlete_stats (athlete_id, season_id, points, assists, rebounds, steals, blocks, games_played) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""


#Update Draft Data, Player Stats, School Stats
UPDATE_DRAFT_PICK = """Insert INTO draft_pick(draft_round, round_pick, overall_selection) Values (?, ?, ?) WHERE draft_pick.athlete_id == athlete.athlete_id FROM athlete WHERE f_name=? AND l_name=? AND school_id=?;"""

UPDATE_SCHOOL_STATS = """UPDATE school_stats 
    SET  points = ?, assists = ?, rebounds = ?, blocks = ?, steals = ?, wins =?, losses=?
    WHERE school_id = (SELECT school_id \
        FROM school \
        WHERE school_id = ?
        )
        AND season_id = ?;"""

ADD_ATHLETE_STATS_BY_NAME = """INSERT INTO athlete_stats (
    athlete_id, season_id, points, assists, rebounds, steals, blocks, games_played
)
SELECT 
    athlete_id,          -- pulled from the athlete table
    ?,                   -- season_id
    ?, ?, ?, ?, ?, ?     -- points, assists, rebounds, steals, blocks, games_played 
    FROM athlete 
    WHERE f_name = ? AND l_name = ? AND school_id = ?;"""

#Checks
CHECK_IF_DRAFTED = """select * FROM (SELECT f_name, l_name, school_id FROM athlete 
    JOIN draft_pick ON athlete.athlete_id = draft_pick.athlete_id
    JOIN draft ON draft_pick.draft_id = draft.draft_id 
    WHERE f_name = ? AND l_name = ? AND drafted = Y);"""


# Delete
DELETE_ATHLETE_BY_NAME = """DELETE FROM athlete WHERE f_name = ? AND l_name = ? AND school_id = ?;"""

#Select players, school, or by rank
VIEW_ALL_ATHLETES = """SELECT athlete_id, f_name, last_name, school_id FROM athlete WHERE f_name = ? AND l_name = ? AND school_id = ?;"""

VIEW_ALL_ATHLETE_STATS = "SELECT * FROM athlete_stats;" #VIEW ALL PLAYER STATS

VIEW_POSITION_STATS = """SELECT * FROM athlete_stats JOIN athlete ON athlete.athlete_id = athlete_stats.athlete_id JOIN position ON athlete.position_id = position.position_id WHERE position.position_id = '?';"""

VIEW_SCHOOLS = """SELECT * FROM school;"""

VIEW_ALL_SCHOOLS_STATS = """SELECT * FROM school_stats JOIN school ON school.school_id = school_stats.school_id;"""

VIEW_CONFERENCE_AVG = """SELECT * FROM school_stats JOIN school ON school.school_id = school_stats.school_id WHERE school.school_conference = '?';"""


# |------------- REQUIRED QUERIES -------------|
#Insert new players, teams, and seasons --- DONE
#Add new draft data for a player who already exists.
#Check if player participated in the draft
#Remove players


#View player statistics compared to team statistics.
#View player statistics compared to league average.
#View player statistics for specific positions
#View players ranked by a specific statistic.





