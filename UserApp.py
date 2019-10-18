import sys
import Back_Database
import Check_Functions

#Database initialize
Back_Database.createDB()

#Insert the Fiscal Code to login.
CFUSER = input("Insert your Fiscal Code to login: ")

#Check if the Fiscal Code is in the database.
#Otherwise, you can register it as a new user.
if not Check_Functions.check_user(CFUSER):
    #Insert new uder after checks.
    REGISTER = input("Fiscal Code doesn't exist! Do you want to register as new user? (y/n): ")

    while REGISTER not in ('y', 'n'):
        REGISTER = input("Error! You have to answer only 'y' or 'n'!: ")

    if REGISTER == "n":
        print("Thanks to visit us")
        sys.exit()
    #Insert a new Fiscal Code and check it.
    CF = input("Please insert your Fiscal Code: ")
    CF_CHECKED = Check_Functions.check_codice_fiscale(CF)
    while(CF_CHECKED) is False:
        CF = input("Error: Fiscal code invalid. Please reinsert it: ")
        CF_CHECKED = Check_Functions.check_codice_fiscale(CF)

    #Insert a new Name and check it.
    NAME = input("Please insert your Name: ")
    NAME_CHECKED = Check_Functions.check_nome(NAME)
    while (NAME_CHECKED) is False:
        NAME = input("Error: Name invalid. Please reinsert it: ")
        NAME_CHECKED = Check_Functions.check_nome(NAME)

    #Insert a new Surname and check it.
    SURNAME = input("Please insert your Surname: ")
    SURNAME_CHECKED = Check_Functions.check_cognome(SURNAME)
    while(SURNAME_CHECKED) is False:
        SURNAME = input("Surname invalid. Please reinsert it: ")
        SURNAME_CHECKED = Check_Functions.check_cognome(SURNAME)

    #Insert age and check it.
    AGE = input("Please insert your Age: ")
    AGE_CHECKED = Check_Functions.check_eta(int(AGE))
    while(AGE_CHECKED) is False:
        AGE = input("Age invalid. Please reinsert it: ")
        AGE_CHECKED = Check_Functions.check_eta(int(AGE))

print("In wich cinema you want to go?")

CINEMA = Back_Database.select_cinema()
for row in CINEMA:
    print("|| " + str(row[0]) + " || " + str(row[1]) + " || " + str(row[2]) + \
        " || ")
CHOICE = input("You want to go to the cinema n°: ")

#Check if the Cinema Id inserted is correct.
CHOICE_CHECK = Check_Functions.check_number_cinema(int(CHOICE))
while(CHOICE_CHECK) is False:
    CHECK = input("Error: Cinena invalid. Please reinsert it: ")
    CHOICE_CHECK = Check_Functions.check_number_cinema(int(CHOICE))

print("What movie do you want to see?")

Film = Back_Database.select_film()
for row in Film:
    print("|| " + str(row[0]) + " || " + str(row[1]) + " || " + str(row[2]) + \
        " || ")
CHOICE = input("You want to see the film n°: ")
#Check if the Film id is correct.
CHOICE_CHECK = Check_Functions.check_number_film(int(CHOICE))
while(CHOICE_CHECK) is False:
    CHECK = input("Error: Film invalid. Please reinsert it: ")
    CHOICE_CHECK = Check_Functions.check_number_film(int(CHOICE))
'''
    while(PLATE_OK) is False:
        PLATE = input("Error: Plate invalid. Please reinsert it: ")
        PLATE_OK = database_functions.check_plate(PLATE)

    PLATE_EXISTING = database_functions.check_plate_existing(PLATE)

END_DATE = input("Please insert the date until you want to rent the car (yyyy-mm-dd): ")
END_DATE_OK = database_functions.check_end_date(END_DATE)

while(END_DATE_OK) is False:
    END_DATE = input("Error: date inserted is not valid. Please reinsert it: ")
    END_DATE_OK = database_functions.check_end_date(END_DATE)

#Add the new rent to database.
database_functions.add_rent(USER, PLATE, END_DATE)

print("Thank you for having rent a car!")
'''
#USER LOGIN
#LISTA DI AUTO
#NOLEGGIA UN'AUTO INSERENDO LA TARGA
#INSERISCI LA DATA DI TERMINE NOLEGGIO
#NOLEGGIO CONFERMATO! VUOI NOLEGGIARE UN'ALTRA AUTO