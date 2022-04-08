import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"Precipitation by Date:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"Station Information:<br/>"
        f"/api/v1.0/stations<br/>"
        f"Dates and temperature observations of the most active station for the last year of data.<br/>"
        f"/api/v1.0/tobs<br/>"
        f"Minimum, Maximum and Average Temperature observations of the most active station for a specified start and end date.</br>"
        f'Please enter dates between 2010-01-01 and 2017-08-23.<br/>'
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"

    )


@app.route("/api/v1.0/precipitation")
def names():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Convert the query results to a dictionary 
    using `date` as the key and `prcp` as the value."""
    # Query all passengers
    results = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    precipitation = []
    for date, prcp in results:
        precipitation_dict = {}
        precipitation_dict[date] = prcp
        precipitation.append(precipitation_dict)

    return jsonify(precipitation)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of the stations from the dataset."""
    # Query all stations.
    station = session.query(Station.station).all()

    session.close()

    # Convert list of tuples into normal list
    stations = list(np.ravel(station))

    return jsonify(stations)


@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Query the dates and temperature observations of the most active station for the last year of data."""
    time_delta_one_year = dt.datetime(2017 , 8, 23) -dt.timedelta(days=365)
    station_temp = session.query(Measurement.tobs).filter(Measurement.date >= time_delta_one_year).\
        filter(Measurement.station == "USC00519281").order_by(Measurement.date.desc()).all()

    session.close()

    # Convert list of tuples into normal list
    station_temps = list(np.ravel(station_temp))

    return jsonify(station_temps)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def startend(start, end=None):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Query the dates and max, min and avg temperature observations of the most active station for a specified start and end date."""
    if end:
        startend = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.station == "USC00519281").filter(Measurement.date >= start).filter(Measurement.date <= end).group_by(Measurement.station).all()

    else:
        startend = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.station == "USC00519281").filter(Measurement.date >= start).group_by(Measurement.station).all()
    session.close()

    # Convert list of tuples into normal list
    startends = list(np.ravel(startend))

    return jsonify(startends)

if __name__ == '__main__':
    app.run(debug=True)
yy