(This is a work-in-progress project. To see the result, please come back next week)
DU - DA Module 10
--------------------------------
--------------------------------
SQLAlchemy Challenge (Using SQLite)
--------------------------------
--------------------------------
by Laura Vara
--------------------------------
NOTE: 

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
    - climate_starter.ipynb file <-- This file is the starter code for the Analysis. It's blank
    - app.py file <-- This is the Flask file
    - Resources directory:
      - hawaii.sqlite
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

----------------------------------------
