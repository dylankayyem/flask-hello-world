import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
	conn = psycopg2.connect("postgres://mypostgresql_25z3_user:EzQfeinYSvvORXtwG96xFoL6F1os5OSN@dpg-cj43gbh8g3nakvhhg5gg-a/mypostgresql_25z3")
	conn.close()
	return "Database Connection Successful"

@app.route('/db_create')
def creating():
	conn = psycopg2.connect("postgres://mypostgresql_25z3_user:EzQfeinYSvvORXtwG96xFoL6F1os5OSN@dpg-cj43gbh8g3nakvhhg5gg-a/mypostgresql_25z3")
	cur = conn.cursor()
	cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
		First varchar(255),
		Last varchar(255),
		City varchar(255),
		Name varchar(255),
		Number int
		);
	''')
	conn.commit()
	conn.close()
	return "Basketball Table Succesfully Created"
	