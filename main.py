import database

menu = '''
What would you like to do?
1.  ADD ATHLETE
2.  ADD ATHLETE STATS
3.  UPDATE ATHLETE STATS
4.  ADD NEW SCHOOL
5.  UPDATE SCHOOL STATS
6.  ADD NEW SEASON
7.  ADD NEW DRAFT
8.  ADD DRAFT PICK
9.  VIEW STATS BY POSITION
10. VIEW ATHLETES RANKED BY STAT
11. VIEW ATHLETE VS CONFERENCE AVERAGES
12. VIEW ATHLETE STATS
13. VIEW ALL ATHLETES
14. EXIT PROGRAM

Your selection: '''

welcome = "Welcome to Stat Tracker!"


# Prompt helpers
def prompt_add_athlete():
    f_name = input("First Name: ").strip()
    l_name = input("Last Name: ").strip()
    position_id = int(input("Position ID (1-5): "))
    school_id = input("School ID (ex. UTK): ").strip().upper()
    height = int(input("Height (inches): "))
    weight = int(input("Weight (lbs): "))
    drafted_input = input("Drafted? (Y/N): ").strip().upper()
    drafted = drafted_input in ("Y", "YES", "TRUE", "1")
    return f_name, l_name, position_id, school_id, height, weight, drafted

def prompt_add_athlete_stats():
    f_name = input("Athlete First Name: ").strip()
    l_name = input("Athlete Last Name: ").strip()
    school_id = input("School ID: ").strip().upper()
    season_id = int(input("Season ID (ex. 2627): "))
    points = int(input("Points: "))
    assists = int(input("Assists: "))
    rebounds = int(input("Rebounds: "))
    steals = int(input("Steals: "))
    blocks = int(input("Blocks: "))
    games_played = int(input("Games Played: "))
    return (f_name, l_name, school_id, season_id,
            points, assists, rebounds, steals, blocks, games_played)

def prompt_update_school_stats():
    school_id = input("School ID (ex. UTK): ").strip().upper()
    season_id = int(input("Season ID (ex. 2627): "))
    points = int(input("Points: "))
    assists = int(input("Assists: "))
    rebounds = int(input("Rebounds: "))
    blocks = int(input("Blocks: "))
    steals = int(input("Steals: "))
    wins = int(input("Wins: "))
    losses = int(input("Losses: "))
    return (school_id, season_id, points, assists, rebounds,
            blocks, steals, wins, losses)

def prompt_add_school():
    school_id = input("School ID (ex. UTK): ").strip().upper()
    school_name = input("School Name: ").strip()
    school_location = input("Location (City, ST): ").strip()
    school_conference = input("Conference: ").strip()
    return school_id, school_name, school_location, school_conference

def prompt_add_season():
    season_id = int(input("Season ID (ex. 2627): "))
    season_year = int(input("Season start year (ex. 2026): "))
    return season_id, season_year

def prompt_add_draft():
    draft_id = input("Draft ID (ex. 0025): ").strip()
    draft_year = int(input("Draft Year: "))
    return draft_id, draft_year

def prompt_add_draft_pick():
    draft_id = input("Draft ID: ").strip()
    athlete_id = int(input("Athlete ID: "))
    draft_round = int(input("Draft Round: "))
    round_pick = int(input("Pick in Round: "))
    overall = int(input("Overall Selection: "))
    return draft_id, athlete_id, draft_round, round_pick, overall

def prompt_position_id():
    return int(input("Position ID (1-5): "))

def prompt_stat_column():
    print("Available stats: points | assists | rebounds | steals | blocks")
    return input("Rank by which stat? ").strip().lower()

def prompt_athlete_name():
    f_name = input("First Name: ").strip()
    l_name = input("Last Name: ").strip()
    return f_name, l_name


# Print helpers
def print_position_stats(rows):
    if not rows:
        print("No stats found for that position.")
        return
    print(f"\n{'ID':<5} {'Name':<20} {'Pos':<4} {'Season':<7} "
          f"{'Pts':>5} {'Ast':>5} {'Reb':>5} {'Stl':>5} {'Blk':>5} {'GP':>4}")
    print("-" * 75)
    for r in rows:
        name = f"{r[1]} {r[2]}"
        print(f"{r[0]:<5} {name:<20} {r[3]:<4} {r[4]:<7} "
              f"{r[5]:>5} {r[6]:>5} {r[7]:>5} {r[8]:>5} {r[9]:>5} {r[10]:>4}")

def print_ranked_athletes(rows, stat):
    print(f"\nRanked by total {stat}:")
    print(f"{'ID':<5} {'Name':<20} {'School':<25} {'Total':>8}")
    print("-" * 60)
    for r in rows:
        name = f"{r[1]} {r[2]}"
        print(f"{r[0]:<5} {name:<20} {r[3]:<25} {r[4]:>8}")

def print_conference_averages(rows):
    if not rows:
        print("Could not find conference averages for this athlete.")
        return
    r = rows[0]
    print(f"\nConference Averages – {r[0]}")
    print(f"{'Stat':<12} {'Average':>10}")
    print("-" * 24)
    print(f"{'Points':<12} {r[1]:>10.1f}")
    print(f"{'Assists':<12} {r[2]:>10.1f}")
    print(f"{'Rebounds':<12} {r[3]:>10.1f}")
    print(f"{'Steals':<12} {r[4]:>10.1f}")
    print(f"{'Blocks':<12} {r[5]:>10.1f}")

def print_athlete_averages(rows):
    if not rows:
        print("No average stats found for this athlete.")
        return
    r = rows[0]
    print(f"\nAthlete Averages – {r[0]} {r[1]}")
    print(f"{'Stat':<12} {'Average':>10}")
    print("-" * 24)
    print(f"{'Points':<12} {r[2]:>10.1f}")
    print(f"{'Assists':<12} {r[3]:>10.1f}")
    print(f"{'Rebounds':<12} {r[4]:>10.1f}")
    print(f"{'Steals':<12} {r[5]:>10.1f}")
    print(f"{'Blocks':<12} {r[6]:>10.1f}")
    print(f"{'Games':<12} {r[7]:>10.1f}")

def print_athlete_stats(rows, f_name, l_name):
    if not rows:
        print("No stats found for that athlete.")
        return
    print(f"\nStats for {f_name} {l_name}:")
    print(f"{'Season':<8} {'Pts':>6} {'Ast':>6} {'Reb':>6} "
          f"{'Stl':>6} {'Blk':>6} {'GP':>5}")
    print("-" * 50)
    for r in rows:
        print(f"{r[3]:<8} {r[4]:>6} {r[5]:>6} {r[6]:>6} "
              f"{r[7]:>6} {r[8]:>6} {r[9]:>5}")

def print_all_athletes(rows):
    print(f"\n{'ID':<5} {'Name':<22} {'Pos':<4} {'School':<28} "
          f"{'Ht':>4} {'Wt':>4} {'Drafted':>8}")
    print("-" * 80)
    for r in rows:
        name = f"{r[1]} {r[2]}"
        drafted = "Yes" if r[7] else "No"
        print(f"{r[0]:<5} {name:<22} {r[3] or '-':<4} {r[4] or '-':<28} "
              f"{r[5] or '-':>4} {r[6] or '-':>4} {drafted:>8}")


# -------------------------------------------------------------------------------------Main------------------------------------------------------------------------
print(welcome)
database.create_tables()

# --------------------------------------------------------------Uncomment once to load synthetic data--------------------------------------------------------------
# database.insert_synthetic_data()

while True:
    user_input = input(menu).strip()

    if user_input == "14":
        print("Goodbye!")
        break

    elif user_input == "1":
        data = prompt_add_athlete()
        database.add_athlete(*data)
        print("Athlete added.")

    elif user_input == "2":
        data = prompt_add_athlete_stats()
        database.add_athlete_stats_by_name(*data)
        print("Athlete stats added.")

    elif user_input == "3":
        data = prompt_add_athlete_stats()   # same fields
        rows = database.update_athlete_stats_by_name(*data)
        print(f"Updated {rows} row(s).")

    elif user_input == "4":
        data = prompt_add_school()
        database.add_school(*data)
        print("School added.")

    elif user_input == "5":
        data = prompt_update_school_stats()
        rows = database.update_school_stats(*data)
        print(f"Updated {rows} school-stats row(s).")

    elif user_input == "6":
        data = prompt_add_season()
        database.add_season(*data)
        print("Season added.")

    elif user_input == "7":
        data = prompt_add_draft()
        database.add_draft(*data)
        print("Draft added.")

    elif user_input == "8":
        data = prompt_add_draft_pick()
        database.add_draft_pick(*data)
        print("Draft pick added.")

    elif user_input == "9":
        pos_id = prompt_position_id()
        rows = database.get_stats_by_position(pos_id)
        print_position_stats(rows)

    elif user_input == "10":
        stat = prompt_stat_column()
        try:
            rows = database.get_athletes_ranked_by_stat(stat)
            print_ranked_athletes(rows, stat)
        except ValueError as e:
            print(e)


    elif user_input == "11":  # VIEW ATHLETE VS CONFERENCE AVERAGES
        f_name, l_name = prompt_athlete_name()
        conf_rows = database.get_conference_averages(f_name, l_name)
        print_conference_averages(conf_rows)

        ath_rows = database.get_athlete_averages(f_name, l_name)
        print_athlete_averages(ath_rows)

    elif user_input == "12":
        f_name, l_name = prompt_athlete_name()
        rows = database.get_athlete_stats(f_name, l_name)
        print_athlete_stats(rows, f_name, l_name)

    elif user_input == "13":
        rows = database.get_all_athletes()
        print_all_athletes(rows)

    else:
        print("Invalid selection. Please try again.")