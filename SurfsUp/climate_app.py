# To execute this app I have to type python climate_app.py  
# Import the dependencies.
from flask import Flask, jsonify
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import datetime as dt

#################################################
# Database Setup
#################################################
# Define the engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session_var = Session(engine)

#################################################
# Flask Setup
#################################################
# Define the Flask application
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
# Define the basic index by using the app.route() method
@app.route("/")


def welcome():
    """List all available api routes."""
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

# Define the 'precipitation' endpoint
@app.route("/api/v1.0/precipitation")


def precipitation():
    """Return a list of the precipitation analysis"""
    # Create session link from Python to the DB of this app route
    session_var = Session(engine)

    # Query Date and Precipitation
    # Find the most recent date in the data set.
    most_recent_date = session_var.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]

    # Calculate the date one year from the last date in data set.
    year_bef_last_date = dt.datetime.strptime(most_recent_date, '%Y-%m-%d').date() - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores (date and prcp)
    precipitation_data = session_var.query(Measurement.date, func.avg(Measurement.prcp)).\
        filter(Measurement.date >= year_bef_last_date).\
        group_by(Measurement.date).all()

    # Convert the query results into a dictionary
    # Convert the query results into a dictionary
    precipitation_dict = {}
    for date, prcp in precipitation_data:
        precipitation_dict[date] = prcp

    # Close the session
    session_var.close()

    # Return the JSON representation of the dictionary
    # return jsonify(precipitation_dict)
    return jsonify({"Date and Precipitation for 1 year": precipitation_dict})


# Define the 'stations' endpoint and return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")


def stations():
    """Return a list of all stations"""
    # Create session link from Python to the DB of this app route
    session_var = Session(engine)

    stations_query = session_var.query(Station.id, Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation).all()

    # Close the Session for this app route
    session_var.close()

    # Create a list of dictionaries to return as a JSON object later on
    all_stations_list = []
    for id, station, name, latitude, longitude, elevation in stations_query:
        stations_dict = {}
        stations_dict['id'] = id
        stations_dict['station'] = station
        stations_dict['name'] = name
        stations_dict['latitude'] = latitude
        stations_dict['longitude'] = longitude
        stations_dict['elevation'] = elevation
        all_stations_list.append(stations_dict)

    # Return the JSON representation of the dictionary
    # return jsonify(all_stations_list)
    return jsonify({"List of Stations": all_stations_list})

# Define the 'tobs' endpoint
@app.route("/api/v1.0/tobs")


def tobs():
    """Return a JSON list of temperature observations for the previous year"""

    # Create session link from Python to the DB of this app route
    session_var = Session(engine)

    # Find the most recent date in the data set.
    most_recent_date = session_var.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]

    # Calculate the date one year from the last date in data set.
    year_bef_last_date = dt.datetime.strptime(most_recent_date, '%Y-%m-%d').date() - dt.timedelta(days=365)

    # Query the dates and tobs of most active station from the previous year
    most_active_stations = session_var.query(Measurement.station, func.count(Measurement.station)). \
        group_by(Measurement.station). \
        order_by(func.count(Measurement.station).desc()).all()

    # Get the most active station id
    most_active_station_id = most_active_stations[0][0]

    # Query for temperature observations for the most active station for the previous year
    temperature_observations = session_var.query(Measurement.date, Measurement.tobs). \
        filter(Measurement.station == most_active_station_id). \
        filter(Measurement.date >= year_bef_last_date).all()

    # Create a list for the tobs
    tobs_list = []
    for date, tobs in temperature_observations:
        tobs_dict = {}
        tobs_list.append({"date": date, "tobs": tobs})

    session_var.close()

    # Return the JSON list of tobs for the previous year
    # return jsonify(tobs_list)
    return jsonify({"Most Active Station": most_active_station_id, "tobs for previous year": tobs_list})

# Define the 'start' endpoint
@app.route("/api/v1.0/<start>")


def date_range(start):
    # Create session link from Python to the DB of this app route
    session_var = Session(engine)

    session_var.close()

# Define the 'start' endpoint
@app.route("/api/v1.0/<start>/<end>")


def date_range_with_end(start, end):
    # Create session link from Python to the DB of this app route
    session_var = Session(engine)

    session_var.close()

# Close the first session
session_var.close()

# Run the Flask application for this app
if __name__ == '__main__':
    app.run(debug=True)


