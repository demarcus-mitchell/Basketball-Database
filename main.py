import database


menu = '''\nWhat would you like to do?
1. Add new athlete.
2. Add new school.
3. Add new season.
4. View athlete stats.
5. View athlete vs league averages.
6. View position stats.
7. View athlete rank by stats.
8. Update athlete stats.\
9. Update athlete demographics.
10. Exit program.

Your selection: '''
welcome = "Welcome to Stat Tracker!"

print(welcome)
database.create_tables()


while (user_input := input(menu)) != "10":
    if user_input == "1":
        pass
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
