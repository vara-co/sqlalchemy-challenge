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
session = Session(engine)

#################################################
# Flask Setup
#################################################
#Define the Flask application
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
    #Create session link from Python to the DB of this app route
    session=Session(engine)

    session.close()

# Define the 'stations' endpoint
@app.route("/api/v1.0/stations")
def stations():
    #Create session link from Python to the DB of this app route
    session=Session(engine)

    session.close()

# Define the 'tobs' endpoint
@app.route("/api/v1.0/tobs")
def tobs():
    #Create session link from Python to the DB of this app route
    session=Session(engine)

    session.close()

# Define the 'start' endpoint
@app.route("/api/v1.0/<start>")
def date_range(start):
    #Create session link from Python to the DB of this app route
    session=Session(engine)

    session.close()

# Define the 'start' endpoint
@app.route("api/v1.0/<start>/<end>")
def date_range_with_end(start, end):
    # Create session link from Python to the DB of this app route
    session = Session(engine)

    session.close()

#Close the first session
session.close()

# Run the Flask application for this app
if __name__ == '__main__':
    app.run(debug=True)
