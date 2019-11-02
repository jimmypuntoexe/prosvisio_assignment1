from flask import Flask, render_template, request
import os
import back_database
import sqlite3

back_database.create_db()
app = Flask(__name__)
_cf = ""
id_cinema = ""
id_film = ""

@app.route("/")
def index():
    connection = sqlite3.connect('ticketapp.db')
    cliente, cinema, film =  back_database.found_table(connection)
    

    return render_template(
        "index.html", main=True, cliente = cliente, cinema = cinema, film = film
    )
    connection.close()

@app.route('/getInfoUser', methods=['GET', 'POST'])
def getInfoUser():
    cf = request.form['codice_fiscale']
    nome = request.form['nome']
    cognome = request.form['cognome']
    age = request.form['età']
    print(cf)
    print(age)

    user = back_database.insert_clienti(cf,nome,cognome, age)
    print(user)
    global _cf
    _cf = cf
    connection = sqlite3.connect('ticketapp.db')
    cliente, cinema, film = back_database.found_table(connection)
    
    

    return render_template(
        "index.html", main=True,
        cliente = cliente,
        cinema = cinema,
        film = film
    )
    connection.close()

@app.route('/getFilm', methods=['GET', 'POST'])
def getFilm():
    id = request.form['film_id']
    connection = sqlite3.connect('ticketapp.db')
    cliente, cinema, film = back_database.found_table(connection)
    global id_film
    id_film = id
    

    return render_template(
        "index.html", main=True,
        cliente = cliente,
        cinema = cinema,
        film = film
    )
    connection.close()

@app.route('/getCinema', methods=['GET', 'POST'])
def getCinema():
    
    id = request.form['cinema_id']
    connection = sqlite3.connect('ticketapp.db')
    cliente, cinema, film = back_database.found_table(connection)
    global id_cinema
    id_cinema = id

    

    return render_template(
        "index.html", main=True,
        cliente = cliente,
        cinema = cinema,
        film = film
    )
    connection.close()





if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
