#!/usr/bin/python3
#import re
import mysql.connector
from mysql.connector import Error
import sqlite3
import datetime
import random
import string


def createDB():
    MYDB = mysql.connector
    try:
        MYDB = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "root",
        )
        if MYDB.is_connected():
            MYCURSOR = MYDB.cursor()
            MYCURSOR.execute("CREATE DATABASE IF NOT EXISTS Biglietteria_Storico")
            MYCURSOR.execute("USE Biglietteria_Storico")
            MYCURSOR.execute("CREATE TABLE IF NOT EXISTS Film (idFilm INT PRIMARY KEY, Titolo VARCHAR(50),Regista VARCHAR(50))")
            MYCURSOR.execute("CREATE TABLE IF NOT EXISTS Cinema (idCinema INT PRIMARY KEY, Nome VARCHAR(50),Città VARCHAR(50))")
            MYCURSOR.execute("CREATE TABLE IF NOT EXISTS Cliente (CF VARCHAR(16) PRIMARY KEY, Cognome VARCHAR(50),Nome VARCHAR(50), Età INT)")
            MYCURSOR.execute("CREATE TABLE IF NOT EXISTS Biglietto (Posto INT, Fila VARCHAR(1),sala INT, data DATETIME PRIMARY KEY, idCinema INT, idFilm INT, CF VARCHAR(45), FOREIGN KEY(idCinema) REFERENCES Cinema(idCinema), FOREIGN KEY(idFilm) REFERENCES Film(idFilm),FOREIGN KEY(CF) REFERENCES Cliente(CF))")
            default_values(MYCURSOR,MYDB)
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (MYDB.is_connected()):
            MYCURSOR.close()
            MYDB.close()
            print("MySQL connection is closed")






def default_values(CURSOR,MYDB):
    CINEMA = [("1","The Space","Vimercate"),("2","Arcadia","Bellinzago"),("3","The movie","Busnago"),("4","The Space","Torino"),("5","Arcadia","Melzo")]
    FILM = [("1","Armagheddon","Micheal Bay"),("2","Le iene","Tarantino"),("3","Pulp Fiction","Tarantino"),("4","Transformers","Micheal Bay"),
    ("5","Il signore degli anelli","Peter Jackson"),("6","Avengers:end game","Fratelli Russo")]
    CLIENTI = [("CF00000000000001","Alessandro","Guidi","24"),("CF00000000000002","Carlo","Caru","23"),("CF00000000000003","Andrea","Carubelli","23"),("CF00000000000004","Leo","Lozio","24"),("CF00000000000005","Gimmy","Baldu","24"),("CF00000000000006","Mario","Bianchi","45")]
    #Biglietto = [("D",15,"CF1",1,1,8,11/10/2019),("D",16,"CF2",1,1,8,11/10/2019),("E",1,"CF3",1,1,8,11/10/2019),("D",15,"CF4",1,2,2,11/10/2019),("E",1,"CF5",1,2,2,11/10/2019),
    #("G",13,"CF4",2,2,6,7/10/2019),("I",2,"CF4",2,2,6,17/10/2019)]
    SQL_QUERTY_C= """INSERT INTO Cinema (IdCinema, Nome, Città) VALUES (%s, %s, %s) """
    SQL_QUERTY_F= """INSERT INTO Film (IdFilm, Titolo, Regista) VALUES (%s, %s, %s) """
    SQL_QUERTY_CL= """INSERT INTO Cliente (CF, Nome, Cognome, Età) VALUES (%s, %s, %s, %s) """
    #sql_query_B=("""INSERT INTO Biglietto (Posto, Fila, Sala, data, ) VALUES (%d, %s, %s, %d) """)
    try:
        CURSOR.executemany(SQL_QUERTY_C,CINEMA)
        MYDB.commit()
    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))
        MYDB.rollback()

    try:
        CURSOR.executemany(SQL_QUERTY_F,FILM)
        MYDB.commit()
    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))
        MYDB.rollback()
    
    try:
        CURSOR.executemany(SQL_QUERTY_CL,CLIENTI)
        MYDB.commit()
    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))
        MYDB.rollback()


def select_cinema():
    
    #Open database connection.
    CONNECTION = mysql.connector.connect(host='localhost', user='root', passwd = 'root')

    #Prepare a cursor to work with database.
    CURSOR = CONNECTION.cursor()

    #We suppose  that the database has been already created.

    CURSOR.execute("USE Biglietteria_Storico")

    CURSOR.execute("SELECT * from Cinema")
    return CURSOR.fetchall()

def select_film():
    CONNECTION = mysql.connector.connect(host='localhost', user='root', passwd = 'root')
    CURSOR = CONNECTION.cursor()
    CURSOR.execute("USE Biglietteria_Storico")
    CURSOR.execute("SELECT * from Film")
    return CURSOR.fetchall()

def print_biglietto(CF, Cinema, Film):
    POSTO = random.randint(1,25)
    SALA = random.randint(1,10)
    FILA = random.choice(string.ascii_lowercase)
    try:
        MYDB = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "root",
        )
        MYCURSOR = MYDB.cursor()
        MYCURSOR.execute("USE Biglietteria_Storico")
        datetimeB = datetime.datetime.now()
        MYCURSOR.execute("INSERT INTO Biglietto(Posto, Fila,sala, data, idCinema, idFilm , CF) \
            VALUES('"+str(POSTO)+"','"+FILA+"','"+str(SALA)+"','"+str(datetimeB)+"','"+str(Cinema)+"','"+str(Film)+"','"+CF+"')")
        MYDB.commit()
        print("BIGLIETTO IN STAMPA....")
        print(".......................")
        print(".......................")
        print(".......................")
        print("Own: "+CF+" Cinema: "+str(Cinema)+" Movie: "+str(Film)+" Seat: "+str(POSTO)+" Row: "+FILA+" auditorium: "+str(SALA)+" Date: "+str(datetimeB))
        print(".......................")
        print(".......................")
        print(".......................")
        print("Ora è disponibile una nuova operazione")
    except Error as e:
        print("Error while connecting to MySQL", e)
