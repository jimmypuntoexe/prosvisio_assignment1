import sys
import database_functions

#Database initialize
database_functions.initialize_database()

#Insert the Fiscal Code to login.
CFUSER = input("Insert your Fiscal Code to login: ")

#Check if the Fiscal Code is in the database.
#Otherwise, you can register it as a new user.
if not database_functions.check_client(CFUSER):
    #Insert new uder after checks.
    REGISTER = input("Fiscal Code doesn't exist! Do you want to register as new user? (y/n): ")

    while REGISTER not in ('y', 'n'):
        REGISTER = input("Error! You have to answer only 'y' or 'n'!: ")

    if REGISTER == "n":
        print("Thanks to visit us")
        sys.exit()

    #Insert a new Fiscal Code and check it.
    CF = input("Please insert your Fiscal Code: ")
    CF_OK = database_functions.check_fiscal_code(CF)
    while(CF_OK) is False:
        CF = input("Error: Fiscal code invalid. Please reinsert it: ")
        CF_OK = database_functions.check_fiscal_code(FC)
'''
    #Insert a new Name and check it.
    N = input("Please insert your Name: ")
    N_OK = database_functions.check_name(N)
    while (N_OK) is False:
        N = input("Error: Name invalid. Please reinsert it: ")
        N_OK = database_functions.check_name(N)

    #Insert a new Surname and check it.
    S = input("Please insert your Surname: ")
    S_OK = database_functions.check_surname(S)
    while(S_OK) is False:
        S = input("Error: Surname invalid. Please reinsert it: ")
        S_OK = database_functions.check_surname(S)

    #Insert a new Date of Birth and check it.
    D = input("Please insert your Date Of Birth (yyyy-mm-dd): ")
    D_OK = database_functions.check_date(D)
    while(D_OK) is False:
        D = input("Error: Date invalid. Please reinsert it with format YYYY-MM-DD: ")
        D_OK = database_functions.check_date(D)

    #Insert a new Place of Birth and check it.
    P = input("Please insert your Place of Birth: ")
    P_OK = database_functions.check_place_of_birth(P)
    while(P_OK) is False:
        P = input("Error: Place of Birth invalid. Please reinsert it: ")
        P_OK = database_functions.check_place_of_birth(P)

    #Insert a new Sex and check it.
    SEX = input("Please insert your Sex (m/f): ")
    SEX_OK = database_functions.check_sex(SEX)
    while(SEX_OK) is False:
        SEX = input("Error: Sex invalid. Please reinsert it: ")
        SEX_OK = database_functions.check_sex(SEX)

    #Add the new client to database.
    database_functions.add_client(FC, N, S, D, P, SEX)

print("WELCOME TO RENTAL CAR!")
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