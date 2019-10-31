 #!/usr/bin/env python
'''check if parameter are correct'''
import sqlite3

def check_user(user):
    """Check if a client is already insert into database"""
    #Open database connection.
    connection = sqlite3.connect('ticketapp.db')
    users=connection.execute("SELECT CF FROM Cliente")
    check = False
    #Check if  user Fiscal Code is already in the database.
    for row in users:
        if row[0] == user:
            check = True

    return check

def check_nome(nome):
    """Check if a name is valid"""
    if not nome:
        return False
    for char in nome:
        if not (('a' <= char <= 'z') \
            or ('A' <= char <= 'Z')):
            return False

    return True

def check_cognome(cognome):
    """Check if a surname is valid"""
    if not cognome:
        print("Stringa vuota")
        return False
    for char in cognome:
        if not (('a' <= char <= 'z') \
            or ('A' <= char <= 'Z')):
            return False

    return True


def check_eta(age):
    '''check if age is valid'''
    check = True
    if age < 10 or age > 130:
        check = False
    return check

def check_codice_fiscale(code):
    """Check if a fiscal code is valid"""
    check = True
    if len(code) != 16:
        check = False
    return check

def check_number_cinema(cinema):
    '''check if the choice of cinema is correct'''
    check = True
    if cinema < 1 or cinema > 5:
        check = False
    return check

def check_number_film(film):
    '''check if the choice of film is correct'''
    check = True
    if film < 1 or film > 6:
        check = False
    return check
