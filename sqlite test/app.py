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
def sqlite_web_api():
    conn = sqlite3.connect(f'lat_and_lon.sqlite')

    cursor = conn.cursor()

    cursor.execute(f'''SELECT * from hauntings''')

    results = cursor.fetchall()
    ghost_files_db = [{'latitude':result[1], 'longitude':result[2]} for result in results]

    conn.close()
    
    print("responding to /sqlite-web-api route request")
    return jsonify(ghost_files_db)


if __name__ == "__main__":
    app.run(debug=True)    