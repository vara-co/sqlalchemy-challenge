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
    return (
        "<h2>Available Routes for the 'hawaii.sqlite' Dataset created with Flask:</h2><br/>"
        "<h3>List of Precipitation Analysis Results for the last 12 months:</h3><br/>"
        f"/api/v1.0/precipitation<br/><br/>"
        "<h3>List of stations from the dataset hawaii.sqlite:</h3><br/>"
        f"/api/v1.0/stations<br/><br/>"
        "<h3>Dates and temperature observations of the most active station, for last 12 months:</h3><br/>"
        f"/api/v1.0/tobs<br/><br/>"
        "<h3>List of min/max/avr temps for a specified start range:</h3><br/>"
        f"Be sure to follow this format: http://127.0.0.1:5000/api/v1.0/2017-06-23<br/>"
        f"YYYY-MM-DD for the start date. The last date in the database will show automatically.<br/>"
        f"/api/v1.0/&lt;start&gt;<br/><br/>"
        "<h3>List of min/max/avr temps for a specified start-end range:</h3><br/>"
        f"Be sure to follow this format: http://127.0.0.1:5000/api/v1.0/2017-06-30/2017-07-03<br/>"
        f"YYYY-MM-DD for both start and end dates<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;"
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
    return jsonify({"Date and Precipitation for 1 year prior to last date in database": precipitation_dict})


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
    return jsonify({"List of Stations in Hawaii for this Database": all_stations_list})

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
    return jsonify({"Most Active Station": most_active_station_id, "tobs for 1 year prior to the last date in Database": tobs_list})

# Define the 'start' endpoint
@app.route("/api/v1.0/<start>")


def start_date(start):
    # Create session link from Python to the DB of this app route
    session_var = Session(engine)
    """Return a list of TMIN, TMAX, and TAVG from Start Date to end of Dataset"""

    # Find the last date in the database
    most_recent_date = session_var.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]

    tobs_start_date = (
        session_var.query(
            func.min(Measurement.tobs),
            func.max(Measurement.tobs),
            func.avg(Measurement.tobs)
        )
        .filter(Measurement.date >= start)
        .filter(Measurement.date <= most_recent_date)
        .group_by(Measurement.date).all())

    # Close the session
    session_var.close()

    # Create Dictionary with query
    tobs_start_list = []
    for min, max, avg in tobs_start_date:
        tobs_start_dict = {}
        tobs_start_dict["TMIN"] = min
        tobs_start_dict["TMAX"] = max
        tobs_start_dict["TAVG"] = avg
        tobs_start_list.append(tobs_start_dict)

    # Return JSON response
    return jsonify({"Avg/Max/Min Temps from YYYY-MM-DD Entered until the end of the Dataset": tobs_start_list})

# Define the 'start' to 'end' endpoint
@app.route("/api/v1.0/<start>/<end>")


def start_end_date(start, end):
    # Create session link from Python to the DB of this app route
    session_var = Session(engine)
    """Return a list of TMIN, TMAX, and TAVG from Start Date to End Date"""

    # Find the last date in the database
    most_recent_date = session_var.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]

    tobs_startend_date = (
        session_var.query(
            func.min(Measurement.tobs),
            func.max(Measurement.tobs),
            func.avg(Measurement.tobs)
        )
        .filter(Measurement.date >= start)
        .filter(Measurement.date <= end)
        .filter(Measurement.date <= most_recent_date)
        .group_by(Measurement.date).all())

    # Close the session
    session_var.close()

    # Create Dictionary with query
    tobs_startend_list = []
    for min, max, avg in tobs_startend_date:
        tobs_startend_dict = {}
        tobs_startend_dict["TMIN"] = min
        tobs_startend_dict["TMAX"] = max
        tobs_startend_dict["TAVG"] = avg
        tobs_startend_list.append(tobs_startend_dict)

    # Return JSON response
    return jsonify({"Avg/Max/Min Temps from Start Date(YYYY-MM-DD) - End Date(YYYY-MM-DD)": tobs_startend_list})


# Close the first session
session_var.close()

# Run the Flask application for this app
if __name__ == '__main__':
    app.run(debug=True)


