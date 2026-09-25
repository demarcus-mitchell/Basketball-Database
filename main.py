import database


menu = '''\nWhat would you like to do?
1. Add positions.
2. Add new school.
3. Add new season.
4. Add draft.
5. Add athlete.
6. View athlete stats.
7. View athlete vs league averages.
8. View position stats.
9. View athlete rank by stats.
10. Update athlete stats.
11. Update athlete.
12. Exit program.

Your selection: '''
welcome = "Welcome to Stat Tracker!"

#prompts
def prompt_add_positions():
    position_id = input("Position ID: ")
    position_name = input("Position Name: ")

    return position_id, position_name

def prompt_add_new_school():
    school_id = input("School ID: ")
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

def prompt_add_athlete():
    f_name = input("First Name: ")
    l_name = input("Last Name: ")
    position_id = input("Position (1-5): ")
    school_id = input("School (ex. UTK): ")
    height = input("Height (in): ")
    weight = input("Weight (lbs): ")
    draft_id = input("Drafted (Y/N): ")

    return f_name, l_name, position_id, school_id, height, weight, draft_id


#print funcs
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


while (user_input := input(menu)) != "12":
    if user_input == "1":
        position_id, position_name = prompt_add_positions()
        database.add_position(position_id, position_name)

    elif user_input == "2":
        school_id, school_name, school_location, school_conference = prompt_add_new_school()
        database.add_school(school_id, school_name, school_location, school_conference)

    elif user_input == "3":
        season_id, season_year = prompt_add_season()
        database.add_season(season_id, season_year)

    elif user_input == "4":
        draft_id, draft_year = prompt_add_draft()
        database.add_draft(draft_id, draft_year)

    elif user_input == "5":
        f_name, l_name, position_id, height, school, weight, drafted = prompt_add_athlete()
        database.add_athlete(f_name, l_name, position_id, height, school, weight, drafted)

    elif user_input == "6":
        pass
    elif user_input == "7":
        pass
    elif user_input == "8":
        pass
    elif user_input == "9":
        pass
    else:
        print("Invalid selection. Please try again.")
