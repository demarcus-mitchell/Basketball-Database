import sqlite3
import queries
import random

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
def add_draft(draft_id, draft_year):
    with connection:
        connection.execute(queries.ADD_DRAFT, (draft_id, draft_year))
def add_athlete(f_name, l_name, position_id, school_id, height, weight, drafted):
    with connection:
        connection.execute(queries.ADD_ATHLETE, (f_name, l_name, position_id, school_id, height, weight, drafted))
def add_athlete_stats(athlete_id, season_id, points, assists, rebounds, steals, blocks, games_played):
    with connection:
        connection.execute(queries.ADD_ATHLETE_STATS,(athlete_id, season_id, points, assists, rebounds, steals, blocks, games_played))
def add_athlete_stats_by_name(f_name, l_name, school_id, season_id, points, assists, rebounds, blocks, steals, games_played):
    with connection:
        connection.execute(queries.ADD_ATHLETE_STATS_BY_NAME, (season_id, points, assists, rebounds, blocks, steals, games_played, f_name, l_name, school_id))

def add_school_stats(school_id, season_id, points, assists, rebounds, blocks, steals, wins, losses):
    with connection:
        connection.execute(queries.ADD_SCHOOL_STATS, (school_id, season_id, points, assists, rebounds, blocks, steals, wins, losses))


#UPDATE FUNCTIONS

def update_athlete_stats_by_name(f_name, l_name, school_id, season_id, points, assists, rebounds, blocks, steals, games_played):
    with connection:
        connection.execute(queries.ADD_ATHLETE_STATS_BY_NAME, (season_id, points, assists, rebounds, blocks, steals, games_played, f_name, l_name, school_id))

def add_draft_stats(draft_id, athlete_id, draft_round, round_pick, overall_selection):
    with connection:
        connection.execute(queries.ADD_DRAFT_PICK, (draft_id, athlete_id, draft_round, round_pick, overall_selection))

#GET FUNCTIONS



# INSERT SYNTHETIC DATA FUNCTION
def insert_synthetic_data():
    """
    Inserts a complete synthetic dataset:

    - 4 schools  (3 SEC + 1 out-of-conference)
    - 25 athletes (6 per school + 1 extra)
    - 3 seasons  (2425/2024, 2526/2025, 2627/2026)
    - 5 positions
    - 1 draft (0025 / 2025) + 5 draft picks
    - athlete_stats for every athlete × every season
    - school_stats aggregated from the athletes of each school
    """
    random.seed(42)  # reproducible results – remove for fresh random data each run

    # ------------------------------------------------------------------
    # 1. Positions
    # ------------------------------------------------------------------
    positions = [
        (1, "PG"),
        (2, "SG"),
        (3, "SF"),
        (4, "PF"),
        (5, "C"),
    ]
    for pos_id, pos_name in positions:
        add_position(pos_id, pos_name)

    # ------------------------------------------------------------------
    # 2. Seasons
    # ------------------------------------------------------------------
    seasons = [
        (2425, 2024),
        (2526, 2025),
        (2627, 2026),
    ]
    for season_id, year in seasons:
        add_season(season_id, year)

    # ------------------------------------------------------------------
    # 3. Draft
    # ------------------------------------------------------------------
    add_draft("0025", 2025)

    # ------------------------------------------------------------------
    # 4. Schools (3 SEC + 1 out-of-conference)
    # ------------------------------------------------------------------
    schools = [
        ("UTK",  "University of Tennessee", "Knoxville, TN", "Southeastern Conference"),
        ("UKY",  "University of Kentucky",  "Lexington, KY", "Southeastern Conference"),
        ("UGA",  "University of Georgia",   "Athens, GA",    "Southeastern Conference"),
        ("GONZ", "Gonzaga University",      "Spokane, WA",   "West Coast Conference"),
    ]
    for s in schools:
        add_school(*s)

    # ------------------------------------------------------------------
    # 5. Athletes (6 per school = 24 + 1 extra = 25)
    #    Last athlete of each school is marked drafted=True
    # ------------------------------------------------------------------
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

    drafted_athlete_ids = []   # the 5 athletes who get drafted
    athlete_counter = 0

    for school_idx, (school_id, _, _, _) in enumerate(schools):
        for i in range(6):
            pos_id   = random.randint(1, 5)
            height   = random.randint(72, 85)      # inches
            weight   = random.randint(175, 265)
            is_drafted = (i == 5)                  # 6th player of each school is the draft pick

            fname = first_names[athlete_counter]
            lname = last_names[athlete_counter]
            athlete_counter += 1

            # Use the existing function
            add_athlete(fname, lname, pos_id, school_id, height, weight, is_drafted)

            if is_drafted:
                # We need the athlete_id → query it back
                cursor = connection.execute(
                    "SELECT athlete_id FROM athlete WHERE f_name=? AND l_name=? AND school_id=?",
                    (fname, lname, school_id)
                )
                ath_id = cursor.fetchone()[0]
                drafted_athlete_ids.append(ath_id)

    # One extra free-agent style athlete (still attached to a school for FK)
    add_athlete("Jordan", "Reed", 3, "UTK", 79, 210, False)

    # ------------------------------------------------------------------
    # 6. Draft picks (5 total – one from each school)
    # ------------------------------------------------------------------
    for overall, ath_id in enumerate(drafted_athlete_ids, start=1):
        draft_round = 1 if overall <= 3 else 2
        round_pick  = overall if overall <= 3 else overall - 3
        add_draft_stats("0025", ath_id, draft_round, round_pick, overall)

    # ------------------------------------------------------------------
    # 7. Athlete stats (every athlete × every season)
    # ------------------------------------------------------------------
    cursor = connection.execute("SELECT athlete_id FROM athlete")
    all_athlete_ids = [row[0] for row in cursor.fetchall()]

    athlete_stats_data = []   # keep for later aggregation
    for athlete_id in all_athlete_ids:
        for season_id, _ in seasons:
            games_played = random.randint(25, 35)
            points   = random.randint(8, 22) * games_played // 10
            assists  = random.randint(2, 8)  * games_played // 10
            rebounds = random.randint(3, 12) * games_played // 10
            steals   = random.randint(1, 3)  * games_played // 10
            blocks   = random.randint(0, 3)  * games_played // 10

            ADD_ATHLETE_STATS(athlete_id, season_id, points, assists, rebounds, blocks, steals, games_played)
            add_athlete_stats_by_name(
                athlete_id, season_id, points, assists, rebounds, blocks, steals, games_played
            )
            athlete_stats_data.append(
                (athlete_id, season_id, points, assists, rebounds, blocks, steals, games_played)
            )

    # ------------------------------------------------------------------
    # 8. School stats – aggregated from the athletes of each school
    # ------------------------------------------------------------------
    # Map athlete → school
    cur = connection.execute("SELECT athlete_id, school_id FROM athlete")
    athlete_to_school = {row[0]: row[1] for row in cur.fetchall()}

    school_totals = {}  # (school_id, season_id) → dict of sums
    for ath_id, season_id, pts, ast, reb, blk, stl, gp in athlete_stats_data:
        school_id = athlete_to_school[ath_id]
        key = (school_id, season_id)
        if key not in school_totals:
            school_totals[key] = {
                "points": 0, "assists": 0, "rebounds": 0,
                "blocks": 0, "steals": 0
            }
        school_totals[key]["points"]   += pts
        school_totals[key]["assists"]  += ast
        school_totals[key]["rebounds"] += reb
        school_totals[key]["blocks"]   += blk
        school_totals[key]["steals"]   += stl

    # Add wins / losses
    for (school_id, season_id), totals in school_totals.items():
        production = (totals["assists"] + totals["rebounds"] +
                      totals["blocks"] + totals["steals"])
        wins   = min(28, max(9, production // 45 + random.randint(-2, 4)))
        losses = 30 - wins

        # ADD_SCHOOL_STATS(school_id, season_id, points, assists, rebounds, blocks, steals, wins, losses)
        add_school_stats(
            school_id, season_id,
            totals["points"], totals["assists"], totals["rebounds"],
            totals["blocks"], totals["steals"],
            wins, losses
        )

    print("Synthetic data inserted successfully.")
