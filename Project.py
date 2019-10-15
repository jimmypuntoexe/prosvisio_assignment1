#!/usr/bin/python3

import mysql.connector
from mysql.connector import Error
import sqlite3
import datetime

mydb = mysql.connector
try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "root",
    )
    if mydb.is_connected():
        mycursor = mydb.cursor()
        #fare controllo se esiste già il database
        mycursor.execute("CREATE DATABASE IF NOT EXISTS provauno")
        mycursor.execute("USE provauno")
        #da mettere in un altra funzione? #inserire foreing key e controllare come creare chiavi composte
        mycursor.execute("CREATE TABLE IF NOT EXISTS Cinema (idCinema INT AUTO_INCREMENT PRIMARY KEY, Nome VARCHAR(50),Città VARCHAR(50), numsale INT)")
        mycursor.execute("CREATE TABLE IF NOT EXISTS Film (idFilm INT AUTO_INCREMENT PRIMARY KEY, Titolo VARCHAR(50),Regista VARCHAR(50), durata INT, genere VARCHAR(50), anno YEAR)")
        mycursor.execute("CREATE TABLE IF NOT EXISTS Clienti (CF VARCHAR(45) PRIMARY KEY, Cognome VARCHAR(50),Nome VARCHAR(50), Età INT)")
        mycursor.execute("CREATE TABLE IF NOT EXISTS Biglietto (Posto INT, Fila VARCHAR(1),sala INT, data DATETIME PRIMARY KEY, FOREIGN KEY(idCinema) REFERENCES Cinema(idCinema), FOREIGN KEY(idFilm) REFERENCES Cinema(idFilm),FOREIGN KEY(CF) REFERENCES Cinema(CF))")
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()
        print("MySQL connection is closed")