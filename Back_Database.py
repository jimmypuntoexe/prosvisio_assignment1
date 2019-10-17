#!/usr/bin/python3
import re
import mysql.connector
from mysql.connector import Error
import sqlite3
import datetime
import random
import string
import datetime


def createDB():
    mydb = mysql.connector
    try:
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "root",
        )
        if mydb.is_connected():
            mycursor = mydb.cursor()
            mycursor.execute("CREATE DATABASE IF NOT EXISTS Biglietteria_Storico")
            mycursor.execute("USE Biglietteria_Storico")
            mycursor.execute("CREATE TABLE IF NOT EXISTS Film (idFilm INT AUTO_INCREMENT PRIMARY KEY, Titolo VARCHAR(50),Regista VARCHAR(50))")
            mycursor.execute("CREATE TABLE IF NOT EXISTS Cinema (idCinema INT AUTO_INCREMENT PRIMARY KEY, Nome VARCHAR(50),Città VARCHAR(50))")
            mycursor.execute("CREATE TABLE IF NOT EXISTS Cliente (CF VARCHAR(16) PRIMARY KEY, Cognome VARCHAR(50),Nome VARCHAR(50), Età INT)")
            mycursor.execute("CREATE TABLE IF NOT EXISTS Biglietto (Posto INT, Fila VARCHAR(1),sala INT, data DATETIME PRIMARY KEY, idCinema INT, idFilm INT, CF VARCHAR(45), FOREIGN KEY(idCinema) REFERENCES Cinema(idCinema), FOREIGN KEY(idFilm) REFERENCES Film(idFilm),FOREIGN KEY(CF) REFERENCES Cliente(CF))")
            default_values(mycursor,mydb)
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (mydb.is_connected()):
            mycursor.close()
            mydb.close()
            print("MySQL connection is closed")






def default_values(cursor,mydb):
    Cinema = [(1,"The Space","Vimercate"),(2,"Arcadia","Bellinzago"),(3,"The movie","Busnago"),(4,"The Space","Torino"),(5,"Arcadia","Melzo")]
    Film = [(1,"Armagheddon","Micheal Bay"),(2,"Le iene","Tarantino"),(3,"Pulp Fiction","Tarantino"),(4,"Transformers","Micheal Bay"),
    (5,"Il signore degli anelli","Peter Jackson"),(6,"Avengers:end game","Fratelli Russo")]
    Clienti = [("CF00000000000001","Alessandro","Guidi",24),("CF00000000000002","Carlo","Caru",23),("CF00000000000003","Andrea","Carubelli",23),("CF00000000000004","Leo","Lozio",24),("CF00000000000005","Gimmy","Baldu",24),("CF00000000000006","Mario","Bianchi",45)]
    #Biglietto = [("D",15,"CF1",1,1,8,11/10/2019),("D",16,"CF2",1,1,8,11/10/2019),("E",1,"CF3",1,1,8,11/10/2019),("D",15,"CF4",1,2,2,11/10/2019),("E",1,"CF5",1,2,2,11/10/2019),
    #("G",13,"CF4",2,2,6,7/10/2019),("I",2,"CF4",2,2,6,17/10/2019)]
    sql_query_C= """INSERT INTO Cinema (IdCinema, Nome, Città, numsale) VALUES (%d, %s, %s) """
    sql_query_F= """INSERT INTO Film (IdFilm, Titolo, Regista) VALUES (%d, %s, %s) """
    sql_query_Cl= """INSERT INTO Cliente (CF, Nome, Città) VALUES (%s, %s, %s) """
    #sql_query_B=("""INSERT INTO Biglietto (Posto, Fila, Sala, data, ) VALUES (%d, %s, %s, %d) """)
    try:
        cursor.execute(sql_query_C,Cinema)
        mydb.commit()
    except:
        mydb.rollback()

    try:
        cursor.execute(sql_query_F,Film)
        mydb.commit()
    except:
        mydb.rollback()
    
    try:
        cursor.execute(sql_query_Cl,Clienti)
        mydb.commit()
    except:
        mydb.rollback()
        
def check_user(user):
    """Check if a client is already insert into database"""
    #Open database connection.
    connection = mysql.connector.connect(host='localhost', user='root', passwd='root')

    #Prepare a cursor to work with database.
    cursor = connection.cursor()

    #We suppose  that the database has been already created.
    cursor.execute("USE Biglietteria_Storico;")

    cursor.execute("SELECT CF FROM clienti")
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

#Check if Date is valid.
def check_data(DATE):
    """Check if a date is valid"""
    if not DATE:
        return False

    pattern = re.compile("([12]\\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01]))")
    if not bool(pattern.match(DATE)):
        return False

    return True