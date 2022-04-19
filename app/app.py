from flask import Flask, jsonify, render_template, redirect
import os
import sqlite3
import psycopg2 


table_name = "ufo_data"
table_name2 = "haunted_places"
table_name3 = "bigfoot_sightings"
db_name = "haunted_places"

#check if we're running in heroku and my environmental variable exist
# if 'DATABASE_URL' in os.environ:
#     postgres_url = os.environ['DATABASE_URL']
# else:
#     #if we're not running in heroku then try and get my local config password
    
#     postgres_url = f"postgresql://postgres:{password}@127.0.0.1:5433/{db_name}"


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

@app.route('/index.html')
def back_home():
    return render_template('index.html')

@app.route("/api/ufo_json")
def ufo_json():

    conn = sqlite3.connect("..\sqlite test\lat_and_lon.sqlite")
    cursor = conn.cursor()

    cursor.execute(f'''SELECT * from ufo''')

    results = cursor.fetchall()
    ufo_db = [{'description':result[1], 'shape':result[2], 'duration':result[3],'city':result[4],'state':result[5],'date':result[6], 'time':result[7],'latitude':result[8], 'longitude':result[9]} for result in results]

    conn.close()

    print("responding to /postgresql-web-api route request")
    return jsonify(ufo_db)
    
@app.route("/api/haunted_places")
def sqlite_web_api():
    conn = sqlite3.connect('..\sqlite test\lat_and_lon.sqlite')

    cursor = conn.cursor()

    cursor.execute(f'''SELECT * from hauntings''')

    results = cursor.fetchall()
    ghost_files_db = [{'city':result[1], 'country':result[2], 'description':result[3],'location':result[4],'state':result[5],'state_abbrev':result[6],'latitude':result[7], 'longitude':result[8]} for result in results]

    conn.close()

    print("responding to /postgresql-web-api route request")
    return jsonify(ghost_files_db)

@app.route("/api/bigfoot_data")
def bigfoot_json():

    conn = sqlite3.connect("..\sqlite test\lat_and_lon.sqlite")
    cursor = conn.cursor()

    cursor.execute(f'''select * from bigfoot''')
    print("this is a test")
    results = cursor.fetchall()
    bigfoot_db = [{'observed':result[1], 'county':result[2],'state':result[3],'latitude':result[4],'longitude':result[5], 'date':result[6]} for result in results]
    conn.close()

    print("responding to /postgresql-web-api route request")
    return jsonify(bigfoot_db)

if __name__ == '__main__':
    app.run(debug=True)