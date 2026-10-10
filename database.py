import sqlite3
import random
import queries

connection = sqlite3.connect("data.db")
connection.execute("PRAGMA foreign_keys = ON")


# Create
def create_tables():
    with connection:
        connection.execute(queries.CREATE_POSITION_TABLE)
        connection.execute(queries.CREATE_SCHOOL_TABLE)
        connection.execute(queries.CREATE_SEASON_TABLE)
        connection.execute(queries.CREATE_DRAFT_TABLE)
        connection.execute(queries.CREATE_ATHLETE_TABLE)
        connection.execute(queries.CREATE_ATHLETE_STATS_TABLE)
        connection.execute(queries.CREATE_SCHOOL_STATS_TABLE)
        connection.execute(queries.CREATE_DRAFT_PICK_TABLE)


# Add
def add_position(position_id, position_name):
    with connection:
        connection.execute(queries.ADD_POSITION, (position_id, position_name))

def add_school(school_id, school_name, school_location, school_conference):
    with connection:
        connection.execute(queries.ADD_SCHOOL,
                           (school_id, school_name, school_location, school_conference))

def add_season(season_id, season_year):
    with connection:
        connection.execute(queries.ADD_SEASON, (season_id, season_year))

def add_draft(draft_id, draft_year):
    with connection:
        connection.execute(queries.ADD_DRAFT, (draft_id, draft_year))

def add_athlete(f_name, l_name, position_id, school_id, height, weight, drafted):
    with connection:
        connection.execute(queries.ADD_ATHLETE,
                           (f_name, l_name, position_id, school_id, height, weight, drafted))

def add_athlete_stats(athlete_id, season_id, points, assists, rebounds,
                      steals, blocks, games_played):
    with connection:
        connection.execute(queries.ADD_ATHLETE_STATS,
                           (athlete_id, season_id, points, assists, rebounds,
                            steals, blocks, games_played))

def add_athlete_stats_by_name(f_name, l_name, school_id, season_id,
                              points, assists, rebounds, steals, blocks, games_played):
    with connection:
        connection.execute(queries.ADD_ATHLETE_STATS_BY_NAME,
                           (season_id, points, assists, rebounds, steals, blocks, games_played,
                            f_name, l_name, school_id))

def add_school_stats(school_id, season_id, points, assists, rebounds,
                     blocks, steals, wins, losses):
    with connection:
        connection.execute(queries.ADD_SCHOOL_STATS,
                           (school_id, season_id, points, assists, rebounds,
                            blocks, steals, wins, losses))

def add_draft_pick(draft_id, athlete_id, draft_round, round_pick, overall_selection):
    with connection:
        connection.execute(queries.ADD_DRAFT_PICK,
                           (draft_id, athlete_id, draft_round, round_pick, overall_selection))


# Update
def update_athlete_stats_by_name(f_name, l_name, school_id, season_id,
                                 points, assists, rebounds, steals, blocks, games_played):
    with connection:
        cursor = connection.execute(
            queries.UPDATE_ATHLETE_STATS_BY_NAME,
            (points, assists, rebounds, steals, blocks, games_played,
             f_name, l_name, school_id, season_id)
        )
        return cursor.rowcount

def update_school_stats(school_id, season_id, points, assists, rebounds,
                        blocks, steals, wins, losses):
    with connection:
        cursor = connection.execute(
            queries.UPDATE_SCHOOL_STATS,
            (points, assists, rebounds, blocks, steals, wins, losses,
             school_id, season_id)
        )
        return cursor.rowcount


# View / Get
def get_stats_by_position(position_id):
    cursor = connection.cursor()
    cursor.execute(queries.VIEW_POSITION_STATS, (position_id,))
    return cursor.fetchall()

def get_athletes_ranked_by_stat(stat_column):
    allowed = {"points", "assists", "rebounds", "steals", "blocks"}
    if stat_column not in allowed:
        raise ValueError(f"Invalid stat. Allowed: {allowed}")
    query = queries.VIEW_PLAYERS_RANKED_BY_STAT.format(stat_column=stat_column)
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def get_conference_averages(f_name, l_name):
    cursor = connection.cursor()
    cursor.execute(queries.VIEW_CONFERENCE_AVERAGES, (f_name, l_name))
    return cursor.fetchall()

def get_athlete_stats(f_name, l_name):
    cursor = connection.cursor()
    cursor.execute(queries.VIEW_ATHLETE_STATS, (f_name, l_name))
    return cursor.fetchall()

def get_athlete_averages(f_name, l_name):
    cursor = connection.cursor()
    cursor.execute(queries.VIEW_ATHLETE_AVERAGES, (f_name, l_name))
    return cursor.fetchall()

def get_all_athletes():
    cursor = connection.cursor()
    cursor.execute(queries.VIEW_ALL_ATHLETES)
    return cursor.fetchall()


# Checks
def athlete_exists(f_name, l_name, school_id):
    cursor = connection.cursor()
    cursor.execute(queries.CHECK_ATHLETE_EXISTS, (f_name, l_name, school_id))
    return len(cursor.fetchall()) > 0

def school_exists(school_id):
    cursor = connection.cursor()
    cursor.execute(queries.CHECK_SCHOOL_EXISTS, (school_id,))
    return len(cursor.fetchall()) > 0

def season_exists(season_id):
    cursor = connection.cursor()
    cursor.execute(queries.CHECK_SEASON_EXISTS, (season_id,))
    return len(cursor.fetchall()) > 0


# Delete
def delete_athlete(athlete_id):
    with connection:
        connection.execute(queries.DELETE_ATHLETE, (athlete_id,))

def delete_athlete_by_name(f_name, l_name, school_id):
    with connection:
        connection.execute(queries.DELETE_ATHLETE_BY_NAME, (f_name, l_name, school_id))


# Synthetic data
def insert_synthetic_data():
    random.seed(42)

    positions = [(1, "PG"), (2, "SG"), (3, "SF"), (4, "PF"), (5, "C")]
    for pos_id, pos_name in positions:
        add_position(pos_id, pos_name)

    seasons = [(2425, 2024), (2526, 2025), (2627, 2026)]
    for season_id, year in seasons:
        add_season(season_id, year)

    add_draft("0025", 2025)

    schools = [
        ("UTK",  "University of Tennessee", "Knoxville, TN", "Southeastern Conference"),
        ("UKY",  "University of Kentucky",  "Lexington, KY", "Southeastern Conference"),
        ("UGA",  "University of Georgia",   "Athens, GA",    "Southeastern Conference"),
        ("GONZ", "Gonzaga University",      "Spokane, WA",   "West Coast Conference"),
    ]
    for s in schools:
        add_school(*s)

    first_names = [
        "Jalen", "Caleb", "Malik", "Tyler", "Devon", "Isaiah",
        "Kameron", "Jaylen", "Amari", "Zion", "Tre", "Darius",
        "Quincy", "Landon", "Bryce", "Nolan", "Kai", "Miles",
        "Ashton", "Roman", "Carter", "Eli", "Julian", "Owen", "Theo"
    ]
    last_names = [
        "Johnson", "Williams", "Brown", "Davis", "Miller", "Wilson",
        "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "White",
        "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson",
        "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen"
    ]

    drafted_athlete_ids = []
    athlete_counter = 0

    for school_id, _, _, _ in schools:
        for i in range(6):
            pos_id = random.randint(1, 5)
            height = random.randint(72, 85)
            weight = random.randint(175, 265)
            is_drafted = (i == 5)

            fname = first_names[athlete_counter]
            lname = last_names[athlete_counter]
            athlete_counter += 1

            add_athlete(fname, lname, pos_id, school_id, height, weight, is_drafted)

            if is_drafted:
                cursor = connection.execute(
                    "SELECT athlete_id FROM athlete WHERE f_name=? AND l_name=? AND school_id=?",
                    (fname, lname, school_id)
                )
                ath_id = cursor.fetchone()[0]
                drafted_athlete_ids.append(ath_id)

    add_athlete("Jordan", "Reed", 3, "UTK", 79, 210, False)

    for overall, ath_id in enumerate(drafted_athlete_ids, start=1):
        draft_round = 1 if overall <= 3 else 2
        round_pick = overall if overall <= 3 else overall - 3
        add_draft_pick("0025", ath_id, draft_round, round_pick, overall)

    cursor = connection.execute("SELECT athlete_id FROM athlete")
    all_athlete_ids = [row[0] for row in cursor.fetchall()]

    athlete_stats_data = []
    for athlete_id in all_athlete_ids:
        for season_id, _ in seasons:
            games_played = random.randint(25, 35)
            points   = random.randint(8, 22) * games_played // 10
            assists  = random.randint(2, 8)  * games_played // 10
            rebounds = random.randint(3, 12) * games_played // 10
            steals   = random.randint(1, 3)  * games_played // 10
            blocks   = random.randint(0, 3)  * games_played // 10

            add_athlete_stats(athlete_id, season_id, points, assists, rebounds,
                              steals, blocks, games_played)
            athlete_stats_data.append(
                (athlete_id, season_id, points, assists, rebounds, blocks, steals, games_played)
            )

    cursor = connection.execute("SELECT athlete_id, school_id FROM athlete")
    athlete_to_school = {row[0]: row[1] for row in cursor.fetchall()}

    school_totals = {}
    for ath_id, season_id, pts, ast, reb, blk, stl, gp in athlete_stats_data:
        school_id = athlete_to_school[ath_id]
        key = (school_id, season_id)
        if key not in school_totals:
            school_totals[key] = {"points": 0, "assists": 0, "rebounds": 0,
                                  "blocks": 0, "steals": 0}
        school_totals[key]["points"]   += pts
        school_totals[key]["assists"]  += ast
        school_totals[key]["rebounds"] += reb
        school_totals[key]["blocks"]   += blk
        school_totals[key]["steals"]   += stl

    for (school_id, season_id), totals in school_totals.items():
        production = (totals["assists"] + totals["rebounds"] +
                      totals["blocks"] + totals["steals"])
        wins = min(28, max(9, production // 45 + random.randint(-2, 4)))
        losses = 30 - wins
        add_school_stats(school_id, season_id,
                         totals["points"], totals["assists"], totals["rebounds"],
                         totals["blocks"], totals["steals"], wins, losses)

    print("Synthetic data inserted successfully.")