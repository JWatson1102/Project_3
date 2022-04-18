#This setup file creates a sqlite database 
import sqlite3
import pandas as pd
# import config
conn = sqlite3.connect(f'testing.sqlite')

cursor = conn.cursor()

#1) need to read the csv files using pandas into dataframes
haunted_df = pd.read_csv("C:\Users\nalle\Desktop\Homework\Project 3\Project_3\sqlite test\cleandf.csv")
print(haunted_df.head())
#2) need to create for loops that will run through the dataframes and extract the contents
#   into a list of dictionaries

sp_to_en_colors = [{"votes": 62, "color":"red"},
                    {"votes": 24, "color":"orange"},
                    {"votes": 29, "color":"yellow"},
                    {"votes": 18, "color":"green"},
                    {"votes": 44, "color":"blue"},
                    {"votes": 64, "color":"black"},
                    {"votes": 48, "color":"pink"}]



#3) need to adjust code to create appropriately named tables
cursor.execute(f"DROP TABLE IF EXISTS table1")

sql_query = f'''CREATE TABLE table1(
   ID INTEGER PRIMARY KEY AUTOINCREMENT,
   VOTES        INTEGER,
   COLOR        CHAR(50)
);
'''

cursor.execute(sql_query)
conn.commit()
print("Table created successfully........")

#4) need to adjust this code for the corrected table names and load the contents
#   that we had previously extracted
for sp_to_en_color in sp_to_en_colors:
    cursor.execute(f'''INSERT INTO table1(VOTES, COLOR) VALUES 
    ('{sp_to_en_color["votes"]}', 2)''')

conn.commit()
print("Data added successfully........")

cursor.execute(f'''SELECT * from table1''')

results = cursor.fetchall()
print(results)

conn.close()