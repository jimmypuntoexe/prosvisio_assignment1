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
        mydb.close()
        print("MySQL connection is closed")


def default_values(mydb):
    '''Insert default values into database'''
    film = [("1", "Armagheddon", "Micheal Bay"), ("2", "Le iene", "Tarantino"),\
        ("3", "Pulp Fiction", "Tarantino"), ("4", "Transformers", "Micheal Bay"),\
        ("5", "Il signore degli anelli", "Peter Jackson"), ("6", \
        "Avengers:end game", "Fratelli Russo")]
    clienti = [("CF00000000000001", "Alessandro", "Guidi", "24"), \
        ("CF00000000000002", "Carlo", "Caru", "23"), ("CF00000000000003",\
        "Andrea", "Carubelli", "23"), ("CF00000000000004", "Leo", "Lozio",\
        "24"), ("CF00000000000005", "Gimmy", "Baldu", "24"),\
        ("CF00000000000006", "Mario", "Bianchi", "45")]
    sql_querty_c = "INSERT INTO Cinema (IdCinema, Nome, Città) \
        VALUES(?, ?, ?)"
    sql_querty_f = """INSERT INTO Film (IdFilm, Titolo, Regista) \
        VALUES(?, ?, ?) """
    try:
        cinema = [('1', 'The Space', 'Vimercate'), ('2', 'Arcadia', 'Bellinzago'),\
        ('3', 'The movie', 'Busnago'), ('4', 'The Space', 'Torino'),\
        ('5', 'Arcadia', 'Melzo')]
        sql_querty_cl = "INSERT INTO Cliente (CF, Nome, Cognome, Età) \
        VALUES(?, ?, ?, ?) "
        mydb.executemany(sql_querty_c, cinema)
        mydb.commit()
    except Error as error:
        print("Failed to insert record into table {}".format(error))
        mydb.rollback()
    try:
        mydb.executemany(sql_querty_f, film)
        mydb.commit()
    except Error as error:
        print("Failed to insert record into table {}".format(error))
        mydb.rollback()
    try:
        mydb.executemany(sql_querty_cl, clienti)
        mydb.commit()
    except Error as error:
        print("Failed to insert record into table {}".format(error))
        mydb.rollback()

def select_cinema():
    '''return all instance of cinema table'''
    connection = sqlite3.connect('ticketapp.db')
    connection.execute("SELECT * from Cinema")
    return connection
    
def select_film():
    '''return all instance of film table'''
    connection = sqlite3.connect('ticketapp.db')
    connection.execute("SELECT * from Film")
    return connection




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
    
def found_table(connection):
    '''Get the data'''
    clienti = connection.execute("SELECT * FROM Cliente")
    cinema = connection.execute("SELECT * FROM Cinema")
    film = connection.execute("SELECT * FROM Film")
    return clienti, cinema, film


def insert_clienti(cf, nome, cognome, age):
	conn= sqlite3.connect('ticketapp.db')
	try:
		conn.execute("INSERT INTO Cliente (CF, Nome, Cognome, Età) VALUES (?, ?, ?, ?)" (str(cf)
        , str(nome), str(cognome), str(age)))
		conn.commit()
	except:
		conn.close()
		return False
	conn.close()
	return True


'''
def make_ticket(n_seriale,id_rivenditore):
	database = sqlite3.connect('ticketapp.db')
	results = database.execute("SELECT n_vendita FROM vendita ORDER BY n_vendita DESC LIMIT 1")

	n_vendita = 1
	for row in results:
		flag=True;
		while(flag):
			n_vendita = row[0] + 1;
			flag= False;

	try:
		database.execute("INSERT INTO vendita(n_vendita,n_seriale,id_rivenditore) VALUES ('%s', '%s', '%s');" %(n_vendita,n_seriale,id_rivenditore))
		conn.commit()
	except:
		conn.rollback()
		conn.close()
		return False

	conn.close()
	return True
'''


