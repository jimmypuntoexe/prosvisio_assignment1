#!/usr/bin/python3
'''manage database'''
import datetime
import random
import string
import sqlite3
from sqlite3 import Error

def create_db():
    '''create database'''
    try:
        mydb = sqlite3.connect('ticketapp.db')
        mydb.execute("CREATE TABLE IF NOT EXISTS Film (idFilm INT PRIMARY KEY,\
                 Titolo VARCHAR(50),Regista VARCHAR(50))")
        mydb.execute("CREATE TABLE IF NOT EXISTS Cinema (idCinema INT \
                PRIMARY KEY, Nome VARCHAR(50),Città VARCHAR(50))")
        mydb.execute("CREATE TABLE IF NOT EXISTS Cliente (CF VARCHAR(16) \
                 PRIMARY KEY, Cognome VARCHAR(50),Nome VARCHAR(50), Età INT)")
        mydb.execute("CREATE TABLE IF NOT EXISTS Biglietto (Posto INT, \
                Fila VARCHAR(1),sala INT, data DATETIME PRIMARY KEY, idCinema INT,\
                idFilm INT, CF VARCHAR(45), FOREIGN KEY(idCinema) REFERENCES \
                Cinema(idCinema), FOREIGN KEY(idFilm) REFERENCES Film(idFilm),\
                FOREIGN KEY(CF) REFERENCES Cliente(CF))")
        default_values(mydb)
    except Error as err:
        print("Error while connecting to MySQL", err)
    finally:
        if mydb.is_connected():
            mydb.close()
            print("MySQL connection is closed")


def default_values(mydb):
    '''Insert default values into database'''
    cinema = [("1", "The Space", "Vimercate"), ("2", "Arcadia", "Bellinzago"),\
        ("3", "The movie", "Busnago"), ("4", "The Space", "Torino"),\
        ("5", "Arcadia", "Melzo")]
    film = [("1", "Armagheddon", "Micheal Bay"), ("2", "Le iene", "Tarantino"),\
        ("3", "Pulp Fiction", "Tarantino"), ("4", "Transformers", "Micheal Bay"),\
        ("5", "Il signore degli anelli", "Peter Jackson"), ("6", \
        "Avengers:end game", "Fratelli Russo")]
    clienti = [("CF00000000000001", "Alessandro", "Guidi", "24"), \
        ("CF00000000000002", "Carlo", "Caru", "23"), ("CF00000000000003",\
        "Andrea", "Carubelli", "23"), ("CF00000000000004", "Leo", "Lozio",\
        "24"), ("CF00000000000005", "Gimmy", "Baldu", "24"),\
        ("CF00000000000006", "Mario", "Bianchi", "45")]
    sql_querty_c = """INSERT INTO Cinema (IdCinema, Nome, Città) \
        VALUES (%s, %s, %s) """
    sql_querty_f = """INSERT INTO Film (IdFilm, Titolo, Regista) \
        VALUES (%s, %s, %s) """
    sql_querty_cl = """INSERT INTO Cliente (CF, Nome, Cognome, Età) \
        VALUES (%s, %s, %s, %s) """
    try:
        mydb.executemany(sql_querty_c, cinema)
        mydb.commit()
    except Error as error:
        print("Failed to insert record into MySQL table {}".format(error))
        mydb.rollback()
    try:
        mydb.executemany(sql_querty_f, film)
        mydb.commit()
    except Error as error:
        print("Failed to insert record into MySQL table {}".format(error))
        mydb.rollback()
    try:
        mydb.executemany(sql_querty_cl, clienti)
        mydb.commit()
    except Error as error:
        print("Failed to insert record into MySQL table {}".format(error))
        mydb.rollback()

def select_cinema():
    '''return all instance of cinema table'''
    connection = sqlite3.connect('ticketapp.db')
    connection.execute("SELECT * from Cinema")
    return connection.fetchall()

def select_film():
    '''return all instance of film table'''
    connection = sqlite3.connect('ticketapp.db')
    connection.execute("SELECT * from Film")
    return connection.fetchall()

def print_biglietto(cf_cl, cinema, film):
    '''Create ticket'''
    posto = random.randint(1, 25)
    sala = random.randint(1, 10)
    fila = random.choice(string.ascii_lowercase)
    try:
        connection = sqlite3.connect('ticketapp.db')
        datetime_b = datetime.datetime.now()
        connection.execute("INSERT INTO Biglietto(Posto, Fila,sala, data, idCinema, idFilm , CF) \
            VALUES('"+str(posto)+"','"+fila+"','"+str(sala)+"','"+str(datetime_b)+"','" \
            +str(cinema)+"','"+str(film)+"','"+cf_cl+"')")
        connection.commit()
        print("BIGLIETTO IN STAMPA....")
        print(".......................")
        print(".......................")
        print(".......................")
        print("Own: "+cf_cl+" Cinema: "+str(cinema)+" Movie: "+str(film)+" Seat: "+str(posto)+\
            " Row: "+fila+" auditorium: "+str(sala)+" Date: "+str(datetime_b))
        print(".......................")
        print(".......................")
        print(".......................")
        print("Ora è disponibile una nuova operazione")
    except Error as err:
        print("Error while connecting to MySQL", err)
