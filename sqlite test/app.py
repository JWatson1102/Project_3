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
    conn = sqlite3.connect(f'testing.sqlite')

    cursor = conn.cursor()

    cursor.execute(f'''SELECT VOTES, COLOR from table1''')

    results = cursor.fetchall()
    color_data_from_db = [ {"votes": result[0], "color": result[1]} for result in results]

    conn.close()
    
    print("responding to /sqlite-web-api route request")

    return jsonify(color_data_from_db)

if __name__ == "__main__":
    app.run(debug=True)