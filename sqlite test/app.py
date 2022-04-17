from flask import Flask, jsonify, render_template, redirect
import os
import sqlite3
# import psycopg2
from pymongo import MongoClient
import socket

table_name = "color_votes"
db_name = "favorite_color"

app = Flask(__name__)

@app.route("/")
def sqlite_web_api():s
    conn = sqlite3.connect(f'cleandf.sqlite')

    cursor = conn.cursor()

    cursor.execute(f'''SELECT * COLOR from table1''')

    results = cursor.fetchall()
    ghost_files_db = [{"city":result[0], "country":result[1], "description":result[2], "location":result[3], "state":result[4], "state_abbrev":result[5], "longitude":result[6], "latitude":result[7]} for result in results]

    conn.close()
    
    print("responding to /sqlite-web-api route request")
    return jsonify(color_data_from_db)
    if __name__ == "__main__":
    app.run(debug=True)