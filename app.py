from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def home():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="user",
            password="user1981",
            database="exampledb"
        )

        cursor = conn.cursor()
        cursor.execute("SELECT NOW()")
        result = cursor.fetchone()

    except mysql.connector.Error as err:
        return f"<h1>Tietokantavirhe: {err}</h1>"
    finally:
        cursor.close()
        conn.close()

    return render_template('index.html', time=result[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
