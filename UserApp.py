import sys
import Back_Database

#Database initialize
Back_Database.createDB()

#Insert the Fiscal Code to login.
CFUSER = input("Insert your Fiscal Code to login: ")

#Check if the Fiscal Code is in the database.
#Otherwise, you can register it as a new user.
if not Back_Database.check_user(CFUSER):
    #Insert new uder after checks.
    REGISTER = input("Fiscal Code doesn't exist! Do you want to register as new user? (y/n): ")

    while REGISTER not in ('y', 'n'):
        REGISTER = input("Error! You have to answer only 'y' or 'n'!: ")

    if REGISTER == "n":
        print("Thanks to visit us")
        sys.exit()

    #Insert a new Fiscal Code and check it.
    CF = input("Please insert your Fiscal Code: ")
    CF_CHECKED = Back_Database.check_codice_fiscale(CF)
    while(CF_CHECKED) is False:
        CF = input("Error: Fiscal code invalid. Please reinsert it: ")
        CF_CHECKED = Back_Database.check_codice_fiscale(CF)

    #Insert a new Name and check it.
    NAME = input("Please insert your Name: ")
    NAME_CHECKED = Back_Database.check_nome(NAME)
    while (NAME_CHECKED) is False:
        NAME = input("Error: Name invalid. Please reinsert it: ")
        NAME_CHECKED = Back_Database.check_nome(NAME)

    #Insert a new Surname and check it.
    SURNAME = input("Please insert your Surname: ")
    SURNAME_CHECKED = Back_Database.check_cognome(SURNAME)
    while(SURNAME_CHECKED) is False:
        SURNAME = input("Surname invalid. Please reinsert it: ")
        SURNAME_CHECKED = Back_Database.check_cognome(SURNAME)

    #Insert age and check it.
    AGE = input("Please insert your Surname: ")
    AGE_CHECKED = Back_Database.check_eta(AGE)
    while(AGE_CHECKED) is False:
        AGE = input("Age invalid. Please reinsert it: ")
        AGE_CHECKED = Back_Database.check_eta(AGE)
'''
print("In wich cinema you want to go")
print("Here's a list of cars you can rent. Rent a car by tiping the license plate!")
print("||  PLATE  ||  BRAND  ||  MODEL  ||  PRICE  ||")
CARS = database_functions.show_car()
for row in CARS:
    print("|| " + str(row[0]) + " || " + str(row[1]) + " || " + str(row[2]) + \
        " || " + str(row[3]) + " ||")
PLATE = input("You want to rent the car n°: ")

#Check if the plate inserted is correct.
PLATE_OK = database_functions.check_plate(PLATE)
while(PLATE_OK) is False:
    PLATE = input("Error: Plate invalid. Please reinsert it: ")
    PLATE_OK = database_functions.check_plate(PLATE)

#Check if the plate is in the Car table.
PLATE_EXISTING = database_functions.check_plate_existing(PLATE)
while(PLATE_EXISTING) is False:
    PLATE = input("Error: Car ins't available for rent. Please reinsert the car plate: ")
    PLATE_OK = database_functions.check_plate(PLATE)

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

#USER LOGIN
#LISTA DI AUTO
#NOLEGGIA UN'AUTO INSERENDO LA TARGA
#INSERISCI LA DATA DI TERMINE NOLEGGIO
#NOLEGGIO CONFERMATO! VUOI NOLEGGIARE UN'ALTRA AUTO?
'''