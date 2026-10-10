import database

menu = '''\nWhat would you like to do?
1. ADD ATHLETE
2. ADD ATHLETE STATS
3. UPDATE ATHLETE 
4. UPDATE ATHLETE STATS
5. ADD NEW SCHOOL
6. UPDATE SCHOOL STATS
7. ADD NEW SEASON
8. UPDATE DRAFT STATS 
9. ADD NEW DRAFT
10. VIEW STATS BY POSITION
11. VIEW ATHLETES RANKED BY (Stat)
12. VIEW ATHLETE VS CONFERENCE AVERAGES
13. VIEW ATHLETE STATS
14. EXIT PROGRAM

Your selection: '''
welcome = "Welcome to Stat Tracker!"

# Prompt funcs
def prompt_add_athlete():
    f_name = input("First Name: ").strip()
    l_name = input("Last Name: ").strip()
    position_id = int(input("Position (1-5): "))
    school_id = input("School ID(ex. UTK): ").strip().upper()
    height = int(input("Height (in): "))
    weight = int(input("Weight (lbs): "))
    drafted_input = input("Drafted (Y/N): ").strip().upper()
    drafted = drafted_input in ("Y", "Yes", "True", "1")

    return f_name, l_name, position_id, school_id, height, weight, drafted

def prompt_add_athlete_stats():
    f_name = input("Athlete First Name: ").strip()
    l_name = input("Athlete Last Name: ").strip()
    school_id = input("School ID: ").strip().upper()
    season_id = int(input("Season ID: (EX: 2627): "))
    points = int(input("Points Scored: " ))
    assists = int(input("Assists: "))
    rebounds = int(input("Rebounds: "))
    blocks = int(input("Blocks: "))
    steals = int(input("Steals :"))
    games_played = int(input("Games Played: "))

    return f_name, l_name, school_id, season_id, points, assists, rebounds, steals, blocks, games_played
def prompt_update_athlete_stats():
    return prompt_add_athlete_stats()

def prompt_add_positions():
    position_id = input("Position ID: ")
    position_name = input("Position Name: ")

    return position_id, position_name

def prompt_add_school():
    school_id = input("School ID(ex. UTK): ").strip().upper()
    school_name = input("School Name: ").strip()
    school_location = input("School State: ").strip()
    school_conference = input("Conference Name: ").strip()

    return school_id, school_name, school_location, school_conference

def prompt_add_season():
    season_id= int(input("Competitive season (Ex: 2627): "))
    season_year = int(input("Season start year: "))
    return season_id, season_year

def prompt_add_draft():
    draft_id = input("Draft ID: ").strip()
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
    stat_rank = input("Which stat would you like to rank by: points, assists, rebounds, steals, blocks").strip().lower()
    return stat_rank


#View funcs
def print_positions(positions):
    print("|---------Positions--------|")
    for position_id, position_name in positions:
        print(f"{position_id}: {position_name}")
    print("|--------------------------|")

def print_schools(school):
    print("|--------Schools--------|")
    for school_name, school_conference in school:
        print(f"{school_name} is in {school_conference}.")
    print("|-----------------------|")


# <------------


print(welcome)
database.create_position_table()
database.create_season_table()
database.create_school_table()
database.create_draft_table()
database.create_athlete_table()
database.create_athlete_stats_table()
database.create_school_stats_table()
database.create_draft_pick_table()


#database.insert_synthetic_data() #CREATES THE SYNTHETIC DATA
"""^^^ To INSERT SYNTHETIC DATA UNCOMMENT OUT  ^^^"""

while True:
    user_input = input(menu).strip()

    if user_input == "14":
        print("Goodbye!")
        break

    elif user_input == "1":          # ADD ATHLETE
        data = prompt_add_athlete()
        database.add_athlete(*data)
        print("Athlete added.")

    elif user_input == "2":          # ADD ATHLETE STATS
        data = prompt_add_athlete_stats()
        database.add_athlete_stats_by_name(*data)
        print("Athlete stats added.")

    elif user_input == "3":          # UPDATE ATHLETE STATS
        data = prompt_update_athlete_stats()
        rows = database.update_athlete_stats_by_name(*data)
        print(f"Updated {rows} row(s).")

    elif user_input == "4":          # ADD NEW SCHOOL
        data = prompt_add_school()
        database.add_school(*data)
        print("School added.")

    elif user_input == "5":  # UPDATE SCHOOL STATS
        print("UPDATE SCHOOL STATS – not yet implemented.")
        # TODO: add prompt + database.update_school_stats(...)

    elif user_input == "6":  # ADD NEW SEASON
        data = prompt_add_season()
        database.add_season(*data)
        print("Season added.")

    elif user_input == "7":  # ADD NEW DRAFT
        data = prompt_add_draft()
        database.add_draft(*data)
        print("Draft added.")


    elif user_input == "8":  # ADD DRAFT PICK
        data = prompt_add_draft_pick()
        database.add_draft_stats(*data)  # your existing function name
        print("Draft pick added.")

    elif user_input == "9":
        pass
    elif user_input == "7":
        pass
    elif user_input == "8":
        pass
    elif user_input == "9":
        pass
    else:
        print("Invalid selection. Please try again.")



