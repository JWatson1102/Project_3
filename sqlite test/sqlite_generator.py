import sqlite3
import pandas as pd
# import config

conn = sqlite3.connect(f'lat_and_lon.sqlite')

cursor = conn.cursor()

#1) need to read the csv files using pandas into dataframes
haunted_df = pd.read_csv(r'sqlite test\cleandf.csv')
ufo_df = pd.read_csv(r'sqlite test\UFO_data.csv')
bigfoot_df = pd.read_csv(r'sqlite test\cleaned_bigfoot.csv')

ufo_df = ufo_df.head(50000)

#haunted_list
haunted_list = []

city_list = haunted_df['city'].to_list()
country_list = haunted_df['country'].to_list()
description_list = haunted_df['description'].to_list()
location_list = haunted_df['location'].to_list()
state_list = haunted_df['state'].to_list()
state_abbrev_list = haunted_df['state_abbrev'].to_list()
lon_list = haunted_df['longitude'].to_list()
lat_list = haunted_df['latitude'].to_list()


for x in range(len(lat_list)):
    haunted_list.append({'city':city_list[x], 'country':country_list[x], 'description':description_list[x], 'location':location_list[x], 'state':state_list[x], 'state_abbrev':state_abbrev_list[x], 'longitude':lon_list[x], 'latitude':lat_list[x]})



#bigfoot_list
bigfoot_list = []

observed_list = bigfoot_df['observed'].to_list()
county_list = bigfoot_df['county'].to_list()
state_list = bigfoot_df['state'].to_list()
lat_list = bigfoot_df['latitude'].to_list()
lon_list = bigfoot_df['longitude'].to_list()
date_list = bigfoot_df['date'].to_list()


for x in range(len(lat_list)):
    bigfoot_list.append({'observed':observed_list[x], 'county':county_list[x], 'state':state_list[x], 'latitude':lat_list[x], 'longitude':lon_list[x], 'date':date_list[x]})



#ufo_list
ufo_list = []

description_list = ufo_df['Description'].to_list()
shape_list = ufo_df['Shape'].to_list()
duration_list = ufo_df['Duration'].to_list()
city_list = ufo_df['City'].to_list()
state_list = ufo_df['State'].to_list()
date_list = ufo_df['Date'].to_list()
time_list = ufo_df['Time'].to_list()
lat_list = ufo_df['Latitude'].to_list()
lon_list = ufo_df['Longitude'].to_list()



for x in range(len(lat_list)):
    ufo_list.append({'description':description_list[x], 'shape':shape_list[x], 'duration':duration_list[x], 'city':city_list[x], 'state':state_list[x], 'date':date_list[x], 'time':time_list[x], 'latitude':lat_list[x], 'longitude':lon_list[x]})





#for haunted
cursor.execute(f"DROP TABLE IF EXISTS hauntings")

sql_query = f'''CREATE TABLE hauntings(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    city varchar,
    country varchar,
    description varchar,
    location varchar,
    state varchar,
    state_abbrev varchar,
    latitude decimal,
    longitude decimal
);
'''
cursor.execute(sql_query)
conn.commit()
print("Table created successfully........")



for hauntings in haunted_list:
    cursor.execute(f'''INSERT INTO hauntings(city, country, description, location, state, state_abbrev, latitude, longitude) VALUES 
    (?, ?, ?, ?, ?, ?, ?, ?)''', (hauntings["city"], hauntings["country"], hauntings["description"], hauntings["location"],  hauntings["state"], hauntings["state_abbrev"], hauntings["latitude"], hauntings["longitude"]))
    #('{hauntings["city"]}', '{hauntings["country"]}', '{hauntings["description"]}', '{hauntings["location"]}', '{hauntings["state"]}', '{hauntings["state_abbrev"]}', '{hauntings["latitude"]}', '{hauntings["longitude"]}')''')

conn.commit()
print("Data added successfully........")

cursor.execute(f'''SELECT * from hauntings''')

results = cursor.fetchall()
print(results)




#for bigfoot
cursor.execute(f"DROP TABLE IF EXISTS bigfoot")

sql_query = f'''CREATE TABLE bigfoot(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    observed varchar,
    county varchar,
    state varchar,
    latitude decimal,
    longitude decimal,
    date varchar
    );
'''
cursor.execute(sql_query)
conn.commit()
print("Table created successfully........")



for bigfoot in bigfoot_list:
    cursor.execute(f'''INSERT INTO bigfoot(observed, county, state, latitude, longitude, date) VALUES 
    (?, ?, ?, ?, ?, ?)''', (bigfoot["observed"], bigfoot["county"], bigfoot["state"], bigfoot["latitude"], bigfoot["longitude"], bigfoot["date"]))
    # ('{bigfoot["observed"]}', '{bigfoot["county"]}', '{bigfoot["state"]}', '{bigfoot["latitude"]}', '{bigfoot["longitude"]}', '{bigfoot["date"]}')''')

conn.commit()
print("Data added successfully........")

cursor.execute(f'''SELECT * from bigfoot''')

results = cursor.fetchall()
print(results)





#for ufo
cursor.execute(f"DROP TABLE IF EXISTS ufo")

sql_query = f'''CREATE TABLE ufo(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    description varchar,
    shape varchar,
    duration varchar,
    city varchar,
    state varchar,
    date varchar,
    time varchar,
    latitude decimal,
    longitude decimal
    
    );
'''
cursor.execute(sql_query)
conn.commit()
print("Table created successfully........")




for ufo in ufo_list:
    cursor.execute(f'''INSERT INTO ufo(description, shape, duration, city, state, date, time, latitude, longitude) VALUES 
    (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (ufo["description"], ufo["shape"], ufo["duration"], ufo["city"],  ufo["state"], ufo["date"], ufo["time"], ufo["latitude"], ufo["longitude"]))
#   ('{ufo["description"]}', '{ufo["shape"]}', '{ufo["duration"]}', '{ufo["city"]}', '{ufo["state"]}', '{ufo["date"]}', '{ufo["time"]}', '{ufo["latitude"]}', '{ufo["longitude"]}')''')

conn.commit()
print("Data added successfully........")

cursor.execute(f'''SELECT * from ufo''')

results = cursor.fetchall()
print(results)

conn.close()
