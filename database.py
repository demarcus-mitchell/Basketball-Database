import sqlite3
import queries

connection = sqlite3.connect("data.db")

# CREATE FUNCTIONS
def create_position_table():
    with connection:
        connection.execute(queries.CREATE_POSITION_TABLE)
def create_season_table():
    with connection:
        connection.execute(queries.CREATE_SEASON_TABLE)
def create_school_table():
    with connection:
        connection.execute(queries.CREATE_SCHOOL_TABLE)
def create_draft_table():
    with connection:
        connection.execute(queries.CREATE_DRAFT_TABLE)
def create_athlete_table():
    with connection:
        connection.execute(queries.CREATE_ATHLETE_TABLE)
def create_athlete_stats_table():
    with connection:
        connection.execute(queries.CREATE_ATHLETE_STATS_TABLE)
def create_school_stats_table():
    with connection:
        connection.execute(queries.CREATE_SCHOOL_STATS_TABLE)
def create_draft_pick_table():
    with connection:
        connection.execute(queries.CREATE_DRAFT_PICK_TABLE)

# ADD FUNCTIONS(Seasons, Positions, Schools, Drafts, Athletes)
def add_season(season_id, season_year):
    with connection:
        connection.execute(queries.ADD_SEASON, (season_id, season_year))   
def add_position(position_id, position_name):
    with connection:
        connection.execute(queries.ADD_POSITION, (position_id, position_name))
def add_school(school_id, school_name, school_location, school_conference):
    with connection:
        connection.execute(queries.ADD_SCHOOL, (school_id, school_name, school_location, school_conference))
def add_draft(draft_id, draft_year,):
    with connection:
        connection.execute(queries.ADD_DRAFT, (draft_id, draft_year))
def add_athlete(f_name, l_name, position_id, school_id, height, weight, drafted):
    with connection:
        connection.execute(queries.ADD_ATHLETE, (f_name, l_name, position_id, school_id, height, weight, drafted))

def add_athlete_stats_by_name(athlete_id, season_id, points, assists, rebounds, blocks, steals, games_played):
    with connection:
        connection.execute(queries.ADD_ATHLETE_STATS_BY_NAME, (athlete_id, season_id, points, assists, rebounds, blocks, steals, games_played))

def add_school_stats(school_id, season_id, points, assists, rebounds, blocks, steals, wins, losses):
    with connection:
        connection.execute(queries.ADD_SCHOOL_STATS, (school_id, season_id, points, assists, rebounds, blocks, steals, wins, losses))

# SEARCH FUNCTIONS
def search_athlete(athlete_id, f_name, l_name, school_id):
    with connection:
        cursor = connection.execute(queries.FIND_ATHLETE_ID, 
            (f_name, l_name, school_id, athlete_id))
        return cursor

#UPDATE FUNCTIONS

def update_athlete_stats_by_name(f_name, l_name, season_id, points, assists, rebounds, blocks, steals, games_played):
    with connection:
        cursor = connection.execute(queries.UPDATE_ATHLETE_STATS_BY_NAME, 
            (points, assists, rebounds, blocks, steals, games_played, f_name, l_name, season_id))
        return cursor.rowcount

def add_draft_stats(draft_id, athlete_id, draft_round, round_pick, overall_selection):
    with connection:
        connection.execute(queries.ADD_DRAFT_PICK, (draft_id, athlete_id, draft_round, round_pick, overall_selection))