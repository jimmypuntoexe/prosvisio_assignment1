import mysql.connector
from mysql.connector import Error
import sqlite3
import datetime


def check_user(user):
    """Check if a client is already insert into database"""
    #Open database connection.
    connection = mysql.connector.connect(host='localhost', user='root', passwd='root')

    #Prepare a cursor to work with database.
    cursor = connection.cursor()

    #We suppose  that the database has been already created.
    cursor.execute("USE Biglietteria_Storico;")

    cursor.execute("SELECT CF FROM Cliente")
    users = cursor.fetchall()
    check = False

    #Check if  user Fiscal Code is already in the database.
    for row in users:
        if row[0] == user:
            check = True

    return check


    #Check if Name is valid.
def check_nome(nome):
    """Check if a name is valid"""
    if not nome:
        return False

    for i in range(0, len(nome)):
        if (not(nome[i] >= 'a' and nome[i] <= 'z') \
            and not (nome[i] >= 'A' and nome[i] <= 'Z') \
            and not nome[i] == ' '):
            return False

    return True


#Check if Surname is valid.
def check_cognome(cognome):
    """Check if a surname is valid"""
    if not cognome:
        return False

    for i in range(0, len(cognome)):
        if (not (cognome[i] >= 'a' and cognome[i] <= 'z') \
            and not (cognome[i] >= 'A' and cognome[i] <= 'Z') \
            and not cognome[i] == ' '):
            return False

    return True



def check_eta(age):
    check = True
    if (age < 10 or age > 130) :
        check = False
    return check


#check if fiscal code is valid
def check_codice_fiscale(code):
    """Check if a fiscal code is valid"""
    check = True
    if (len(code) != 16) :
        check = False
    return check


#check if the choice of cinema is correct
def check_number_cinema(cinema) :
    check = True 
    if (cinema <= 1 or cinema > 4 ) :
        check = False
    return check
