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



#print funcs
def print_positions(positions):
    print("|---------Positions--------|")
    for position_id, position_name in positions:
        print(f"{position_id}: {position_name}")
    print("|--------------------------|")



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
        pass
    elif user_input == "3":
        pass
    elif user_input == "4":
        pass
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
    else:
        print("Invalid selection. Please try again.")
