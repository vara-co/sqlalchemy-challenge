DU - DA Module 10
--------------------------------
--------------------------------
SQLAlchemy Challenge (Using SQLite and Flask)
--------------------------------
--------------------------------
by Laura Vara
--------------------------------
NOTE: To use the Flask file, you need to load it on a program like Python. Then you need to run the code as is, and then type your program to run it. Something like 'python file.py' just change the name of the file to my actual flask file. After it runs, it will show a link on the terminal, and that's the link to the app routes. I tested it twice, and it is up and running. You will need to have SQLAlchemy and SQLite installed in your Anaconda Virtual Environment to be able to see, work, and run these files.

---------------------------------
INDEX
---------------------------------
1. Content of the repository
2. Instructions for the SQLAlchemy Challenge
3. References

---------------------------------
Content of the repository
---------------------------------
- SurfsUp directory:
    - climate_LMVSFinal.ipynb file <-- This is the Analysis file I worked on.
    - climate_starter.ipynb file <-- This file is the starter code for the Analysis. It's blank.
    - climate_app.py file <-- This is the Flask app, created via python, with my code for these queries. With the right packages installed, and dependencies imported, it works perfectly well.
    - Resources directory:
      - hawaii.sqlite  <-- this file cannot be opened via Jupyter Notebook. Instead try drag and drop to this site https://sqliteviewer.app/
      - hawaii_measurements.csv
      - hawaii_stations.csv
    - output_data directory:
      - PrecipitationChart.png
      - TemperatureChart.png

----------------------------------
Instructions for SurfsUp
----------------------------------
This Challenge is divided in Two Parts: 'Analyze and Explore the Climate Data' & 'Design Your Climate APP'
- Part 1: Analyze and Explore the Climate Data
    - **PRECIPITATION ANALYSIS:**
    1. Find the most recent date in the dataset.
    2. Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.
Hint: Don’t pass the date as a variable to your query.
    3. Select only the "date" and "prcp" values.
    4. Load the query results into a Pandas DataFrame. Explicitly set the column names.
    5. Sort the DataFrame values by "date".
    6. Plot the results by using the DataFrame plot method, as the image in the starter code shows.
    7. Use Pandas to print the summary statistics for the precipitation data.

    - **STATION ANALYSIS:**
    1. Design a query to calculate the total number of stations in the dataset.
    2. Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:
List the stations and observation counts in descending order.
Hint: You’ll need to use the func.count function in your query.
Answer the following question: which station id has the greatest number of observations?
    3. Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
Hint: You’ll need to use functions such as func.min, func.max, and func.avg in your query.
    4. Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:
        * Filter by the station that has the greatest number of observations.
        * Query the previous 12 months of TOBS data for that station.
        * Plot the results as a histogram with bins=12, as the image in the starter code.
    5. Close your session.
  
* Part 2: DESIGN YOUR CLIMATE APP  (USING FLASK)
Now that you’ve completed your initial analysis, you’ll design a Flask API based on the queries that you just developed. To do so, use Flask to create your routes as follows:

1. /
    * Start at the homepage.
    * List all the available routes

2. /api/v1.0/precipitation
    * Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
    * Return the JSON representation of your dictionary.

3. /api/v1.0/stations
    * Return a JSON list of stations from the dataset.

4. /api/v1.0/tobs
    * Query the dates and temperature observations of the most-active station for the previous year of data.
    * Return a JSON list of temperature observations for the previous year.

5. /api/v1.0/< start > and /api/v1.0/< start >/< end >
    * Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
    * For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
    * For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

**HINTS:** 
- Join the station and measurement tables for some of the queries.
- Use the Flask jsonify function to convert your API data to a valid JSON response object.
----------------------------------------
