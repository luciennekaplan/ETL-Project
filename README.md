# ETL-Project
Blake Ashford, Courtney Robison, Lucy Kaplan, Savannah Cordry

We took UFO and Meteorite Landing data and put it into a SQL Database!

## Extracting the Data
Through the use of kaggle.com we were able to find two CSV files which peaked our interest: one for [UFO sightings](Resources/complete.csv) from the National UFO Reporting Center, and another for [Meteorite landings](Resources/meteorite-landings.csv) from the US Meteoritical Society. These each contained the location, date, and description of the objects. The UFO data also contained comments about the sighting, which was thoroughly entertaining to read through. 

## Transforming the Data
The two csv files we obtained needed some cleaning up before they were ready for anaylysis.  For the UFO data, we had erroneous data that was removed upon being read into python.  We then selected sightings that only occured in the US.  This also removed any incomplete lines of data, or 0.00 lat long values.  We wanted to capture the year that sightings occured.  This meant taking out datetime column and filtering it out to just the year. We then selected the UFO sightings that occured between the years of 1906 to 2013.

The meteorite landing data needed to have the blank years removed as well as any invalid locations.  The information was then filtered by landings that occured between 1906 and 2013.  To determine landings that occured in the US we had to convert lat and long values into zip codes, dropping any lat longs that did not have a zipcode value as they did not occur within the US. To do this, we used [the uszipcode programmable zipcode database](https://pypi.org/project/uszipcode/) for Python. 

## Loading the Data

## How to Run
First, run the meteor-cleanup.py and ufocleanup.py on the [meteorite-landings.csv](Resources/meteorite-landings.csv) and [complete.csv](Resources/complete.csv) files, respectively (found in the Resources folder). This will output two new CSV files with the cleaned and transformed data. Once complete, create a PostgreSQL database using the included schema, then import the two CSV files. Voila!