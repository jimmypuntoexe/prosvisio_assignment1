#!/usr/bin/python3
'''manage database'''
 #!/usr/bin/env python
import datetime
import random
import string
import mysql.connector
from mysql.connector import Error

'''create database'''
def create_db():
    try:
        mydb = mysql.connector.connect(host="localhost", \
            user="root", passwd="root")
        if mydb.is_connected():
            mycursor = mydb.cursor()
            mycursor.execute("CREATE DATABASE IF NOT EXISTS Biglietteria_Storico")
            mycursor.execute("USE Biglietteria_Storico")
            mycursor.execute("CREATE TABLE IF NOT EXISTS Film (idFilm INT PRIMARY KEY,\
                 Titolo VARCHAR(50),Regista VARCHAR(50))")
            mycursor.execute("CREATE TABLE IF NOT EXISTS Cinema (idCinema INT \
                PRIMARY KEY, Nome VARCHAR(50),Città VARCHAR(50))")
            mycursor.execute("CREATE TABLE IF NOT EXISTS Cliente (CF VARCHAR(16) \
                 PRIMARY KEY, Cognome VARCHAR(50),Nome VARCHAR(50), Età INT)")
            mycursor.execute("CREATE TABLE IF NOT EXISTS Biglietto (Posto INT, \
                Fila VARCHAR(1),sala INT, data DATETIME PRIMARY KEY, idCinema INT,\
                idFilm INT, CF VARCHAR(45), FOREIGN KEY(idCinema) REFERENCES \
                Cinema(idCinema), FOREIGN KEY(idFilm) REFERENCES Film(idFilm),\
                FOREIGN KEY(CF) REFERENCES Cliente(CF))")
            default_values(mycursor, mydb)
    except Error as err:
        print("Error while connecting to MySQL", err)
    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()
            print("MySQL connection is closed")

'''Insert default values into database'''
def default_values(cursor, mydb):
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
        cursor.executemany(sql_querty_c, cinema)
        mydb.commit()
    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))
        mydb.rollback()
    try:
        cursor.executemany(sql_querty_f, film)
        mydb.commit()
    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))
        mydb.rollback()
    try:
        cursor.executemany(sql_querty_cl, clienti)
        mydb.commit()
    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))
        mydb.rollback()

'''return all instance of cinema table'''
def select_cinema():
    connection = mysql.connector.connect(host='localhost', user='root', passwd='root')
    cursor = connection.cursor()
    cursor.execute("USE Biglietteria_Storico")
    cursor.execute("SELECT * from Cinema")
    return cursor.fetchall()

'''return all instance of film table'''
def select_film():
    connection = mysql.connector.connect(host='localhost', user='root', passwd='root')
    cursor = connection.cursor()
    cursor.execute("USE Biglietteria_Storico")
    cursor.execute("SELECT * from Film")
    return cursor.fetchall()

'''Create ticket'''
def print_biglietto(cf, cinema, film):
    posto = random.randint(1, 25)
    sala = random.randint(1, 10)
    fila = random.choice(string.ascii_lowercase)
    try:
        mydb = mysql.connector.connect(host="localhost", user="root",\
            passwd="root")
        mycursor = mydb.cursor()
        mycursor.execute("USE Biglietteria_Storico")
        datetime_b = datetime.datetime.now()
        mycursor.execute("INSERT INTO Biglietto(Posto, Fila,sala, data, idCinema, idFilm , CF) \
            VALUES('"+str(posto)+"','"+fila+"','"+str(sala)+"','"+str(datetime_b)+"','" \
            +str(cinema)+"','"+str(film)+"','"+cf+"')")
        mydb.commit()
        print("BIGLIETTO IN STAMPA....")
        print(".......................")
        print(".......................")
        print(".......................")
        print("Own: "+cf+" Cinema: "+str(cinema)+" Movie: "+str(film)+" Seat: "+str(posto)+\
            " Row: "+fila+" auditorium: "+str(sala)+" Date: "+str(datetime_b))
        print(".......................")
        print(".......................")
        print(".......................")
        print("Ora è disponibile una nuova operazione")
    except Error as err:
        print("Error while connecting to MySQL", err)
