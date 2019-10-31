 #!/usr/bin/env python
'''Main function '''

import sys
import back_database
import check_functions

#Database initialize
back_database.create_db()

#Insert the Fiscal Code to login.
CFUSER = raw_input("Insert your Fiscal Code to login: ")

#Check if the Fiscal Code is in the database.
#Otherwise, you can register it as a new user.
if not check_functions.check_user(CFUSER):
    #Insert new uder after checks.
    REGISTER = raw_input("Fiscal Code doesn't exist! Do you want to register as new user? (y/n): ")

    while REGISTER not in ('y', 'n'):
        REGISTER = input("Error! You have to answer only 'y' or 'n'!: ")

    if REGISTER == "n":
        print("Thanks to visit us")
        sys.exit()
    #Insert a new Fiscal Code and check it.
    CFUSER = input("Please insert your Fiscal Code: ")
    CF_CHECKED = check_functions.check_codice_fiscale(CFUSER)
    while(CF_CHECKED) is False:
        CFUSER = input("Error: Fiscal code invalid. Please reinsert it: ")
        CF_CHECKED = check_functions.check_codice_fiscale(CFUSER)

    #Insert a new Name and check it.
    NAME = input("Please insert your Name: ")
    NAME_CHECKED = check_functions.check_nome(NAME)
    while (NAME_CHECKED) is False:
        NAME = input("Error: Name invalid. Please reinsert it: ")
        NAME_CHECKED = check_functions.check_nome(NAME)

    #Insert a new Surname and check it.
    SURNAME = input("Please insert your Surname: ")
    SURNAME_CHECKED = check_functions.check_cognome(SURNAME)
    while(SURNAME_CHECKED) is False:
        SURNAME = input("Surname invalid. Please reinsert it: ")
        SURNAME_CHECKED = check_functions.check_cognome(SURNAME)

    #Insert age and check it.
    AGE = input("Please insert your Age: ")
    AGE_CHECKED = check_functions.check_eta(int(AGE))
    while(AGE_CHECKED) is False:
        AGE = input("Age invalid. Please reinsert it: ")
        AGE_CHECKED = check_functions.check_eta(int(AGE))

print("In wich cinema you want to go?")

CINEMA = back_database.select_cinema()
for row in CINEMA:
    print("|| " + str(row[0]) + " || " + str(row[1]) + " || " + str(row[2]) + \
        " || ")
CINEMA_ID = input("You want to go to the cinema n°: ")

#Check if the Cinema Id inserted is correct.
CHOICE_CHECK = check_functions.check_number_cinema(int(CINEMA_ID))
while(CHOICE_CHECK) is False:
    CHECK = input("Error: Cinena invalid. Please reinsert it: ")
    CHOICE_CHECK = check_functions.check_number_cinema(int(CINEMA_ID))

print("What movie do you want to see?")

FILM = back_database.select_film()
for row in FILM:
    print("|| " + str(row[0]) + " || " + str(row[1]) + " || " + str(row[2]) + \
        " || ")
FILM_ID = input("You want to see the film n°: ")
#Check if the Film id is correct.
CHOICE_CHECK = check_functions.check_number_film(int(FILM_ID))
while(CHOICE_CHECK) is False:
    CHECK = input("Error: Film invalid. Please reinsert it: ")
    CHOICE_CHECK = check_functions.check_number_film(int(FILM_ID))

back_database.print_biglietto(CFUSER, CINEMA_ID, FILM_ID)
