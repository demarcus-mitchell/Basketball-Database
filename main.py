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
    f_name = input("First Name: ")
    l_name = input("Last Name: ")
    position_id = input("Position (1-5): ")
    school_id = input("School ID(ex. UTK): ")
    height = input("Height (in): ")
    weight = input("Weight (lbs): ")
    draft_id = input("Drafted (Y/N): ")

    return f_name, l_name, position_id, school_id, height, weight, draft_id

def prompt_add_athlete_stats():
    season_id = input("Season ID: (EX: 2627): ")
    points = input("Points Scored: " )
    assists = input("Assists: ")
    rebounds = input("Rebounds: ")
    blocks = input("Blocks: ")
    steals = input("Steals :")
    games_played = input("Games Played: ")

    return season_id, points, assists, rebounds, blocks, steals, games_played
def prompt_add_positions():
    position_id = input("Position ID: ")
    position_name = input("Position Name: ")

    return position_id, position_name

def prompt_add_new_school():
    school_id = input("School ID(ex. UTK): ")
    school_name = input("School Name: ")
    school_location = input("School State: ")
    school_conference = input("Conference Name: ")

    return school_id, school_name, school_location, school_conference

def prompt_add_season():
    season_id=  input("Competitive season (Ex: 2627): ")
    season_year = input("Season start year: ")

    return season_id, season_year

def prompt_add_draft():
    draft_id = input("Draft ID: ")
    draft_year = input("Draft Year: ")
    return draft_id, draft_year


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

while (user_input := input(menu)) != "14":
    if user_input == "1":
        f_name, l_name, position_id, school, height, weight, drafted = prompt_add_athlete()
        database.add_athlete(f_name, l_name, position_id, school, height, weight, drafted)

    elif user_input == "2":
        season_id, points, assists, rebounds, blocks, steals, games_played = prompt_add_athlete_stats()
        database.add_athlete_stats_by_name(season_id, points, assists, rebounds, blocks, steals, games_played)

    elif user_input == "3":
        season_id, season_year = prompt_add_season()
        database.add_season(season_id, season_year)

    elif user_input == "4":
        draft_id, draft_year = prompt_add_draft()
        database.add_draft(draft_id, draft_year)

    elif user_input == "5":
        pass

    elif user_input == "6":
        pass

    elif user_input == "7":
        pass
    elif user_input == "8":
        pass
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



