from flask import Flask, render_template, request
import os
import back_database
import sqlite3

back_database.create_db()
app = Flask(__name__)

@app.route("/")
def index():
    database = sqlite3.connect('ticketapp.db')
    cursor = database.cursor()
    
    cinema = back_database.select_cinema()
    film = back_database.select_film()
    biglietto = back_database.print_biglietto()

    database.close()

    return render_template(
        "index.html", main=True, car = car, rental = rental, client = client
    )


if __name__ == "__main__":
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host='0.0.0.0', port=port)
    app.run()
