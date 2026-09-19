import sqlite3
import queries


# <------------

connection = sqlite3.connect("data.db")


# Functions

def create_tables():
    with connection:
        connection.execute(CREATE_TABLES)

def add_athlete():
    with connection:
        connection.execute(ADD_ATHLETE)

def add_athlete_stats():
    with connection:
        connection.execute(ADD_ATHLETE_STATS)

def add_position():
    with connection:
        connection.execute(ADD_POSITION)

def add_school():
    with connection:
        connection.execute(ADD_SCHOOL)

def add_school_stats():
    with connection:
        connection.execute(ADD_SCHOOL_STATS)

def add_draft():
    with connection:
        connection.execute(ADD_DRAFT)

def add_draft_stats():
    with connection:
        connection.execute(ADD_DRAFT_PICK)

def add_season():
    with connection:
        connection.execute(ADD_SEASON)