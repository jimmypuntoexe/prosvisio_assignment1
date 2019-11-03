'''webapp'''
import os
import sqlite3
from flask import render_template, Flask, request
import back_database

back_database.create_db()
APP = Flask(__name__)
_CF = ""
ID_CINEMA = ""
ID_FILM = ""

'''return home page'''
@APP.route("/") 
def index():
    connection = sqlite3.connect('ticketapp.db')
    cliente, cinema, film = back_database.found_table(connection)
    connection.close()
    return render_template(
        "index.html", main=True, cliente=cliente, cinema=cinema, film=film
    )

'''Add client for buy ticket'''
@APP.route('/getreginfouser', methods=['GET', 'POST'])
def getreginfouser():
    codf = request.form['codice_fiscale']
    nome = request.form['nome']
    cognome = request.form['cognome']
    age = request.form['età']
    print(codf)
    print(age)
    user = back_database.insert_clienti(codf, nome, cognome, age)
    print(user)
    global _CF
    #_CF = codf
    connection = sqlite3.connect('ticketapp.db')
    cliente, cinema, film = back_database.found_table(connection)
    connection.close()
    return render_template(
        "index.html", main=True,
        cliente=cliente,
        cinema=cinema,
        film=film
    )

'''Insert ticket and print it '''
@APP.route('/printticket', methods=['GET', 'POST'])
def printticket():
    codf = request.form['codice_fiscale']
    id_c = request.form['cinema_id']
    id_f = request.form['film_id']
    back_database.print_biglietto(codf, id_c, id_f)
    connection = sqlite3.connect('ticketapp.db')
    cliente, cinema, film = back_database.found_table(connection)
    connection.close()
    return render_template(
        "index.html", main=True,
        cliente=cliente,
        cinema=cinema,
        film=film
    )

if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))
    APP.run(host='0.0.0.0', port=PORT)
