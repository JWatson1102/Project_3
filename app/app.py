from flask import Flask, jsonify, render_template, redirect
import os
import sqlite3
import psycopg2
from config import password 
# from datetime import datetime
# epoch = datetime(1970, 1, 1)
# t = datetime(1956, 3, 2)
# diff = t-epoch
# # print diff.days * 24 * 3600 + diff.seconds


table_name = "ufo_data"
table_name2 = "haunted_places"
table_name3 = "bigfoot_sightings"
db_name = "haunted_places"

#check if we're running in heroku and my environmental variable exist
if 'DATABASE_URL' in os.environ:
    postgres_url = os.environ['DATABASE_URL']
else:
    #if we're not running in heroku then try and get my local config password
    
    postgres_url = f"postgresql://postgres:{password}@127.0.0.1:5433/{db_name}"


app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bigfoot_files.html')
def bigfoot():
    return render_template('bigfoot_files.html')

@app.route('/ghost_files.html')
def ghost():
    return render_template('ghost_files.html')

@app.route('/ufo_files.html')
def ufo():
    return render_template('ufo_files.html')

@app.route('/index')
def back_home():
    return render_template('index.html')

@app.route("/api/ufo_json")
def ufo_json():
    # conn = psycopg2.connect
    #     database=db_name, user='postgres', password=postgres_pwd, host='127.0.0.1', port= '5432'
    # 
    conn = psycopg2.connect(postgres_url)
    cursor = conn.cursor()

    cursor.execute(f'''SELECT * from {table_name}''')

    results = cursor.fetchall()
    ufo_db = [ {"Description": result[0], "Shape": result[1],"Duration": result[2], "City": result[3],"State": result[4], "Date": result[5],  "Time": result[6], "Latitude": result[7] , "Longitude":result[8]} for result in results]

    conn.close()

    print("responding to /postgresql-web-api route request")
    return jsonify(ufo_db)
    
@app.route("/api/haunted_places")
def ghost_json():

    conn = psycopg2.connect(postgres_url)
    cursor = conn.cursor()

    cursor.execute(f'''SELECT * from {table_name2}''')

    results = cursor.fetchall()
    ghost_files_db = [{"city":result[0], "country":result[1], "description":result[2], "location":result[3], "state":result[4], "state_abbrev":result[5], "longitude":result[6], "latitude":result[7]} for result in results]

    conn.close()

    print("responding to /postgresql-web-api route request")
    return jsonify(ghost_files_db)

@app.route("/api/bigfoot_data")
def bigfoot_json():

    conn = psycopg2.connect(postgres_url)
    cursor = conn.cursor()

    cursor.execute(f'''select * from {table_name3};''')
    print("this is a test")
    results = cursor.fetchall()
    # print(results)
    bigfoot_db = [{"observed":result[0], "county":result[1], "state":result[2], "latitude":result[3], "longitude":result[4]} for result in results]
    # bigfoot_db = [{"date":result[5]} for result in results]
    conn.close()

    print("responding to /postgresql-web-api route request")
    return jsonify(bigfoot_db)

if __name__ == '__main__':
    app.run(debug=True)