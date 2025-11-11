from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
	#connect to MarianDB
	conn = mysql.connector.connect (
		host="localhost",
		user="user",
		password="user1981",
		database="exampledb"
	)

	cursor = conn.cursor()
	cursor.execute("SELECT NOW()")
	result = cursor.fetchone()

	#clean up
	cursor.close()
	conn.close()


	html = f"""
	<h1>Palvelimen kellonaika {result[0]}</h1>
	<h1>Palvelimen kellonajan saat päivitettyä päivittämällä sivun</h1>
	<h1>Hyvää päivän jatkoa :)</h1>
	<h1>&hearts;&hearts;&hearts;&hearts;&hearts;&hearts;&hearts;</h1>
	"""
	return html
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
