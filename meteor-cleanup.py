import pandas as pd
from citipy import citipy
import os

# Import the raw CSV
path = os.path.join(os.path.dirname(__file__),"Resources","meteorite-landings.csv")
data = pd.read_csv(path)

# Filter out the invalid locations
filter_location = data.dropna()
filter_location = filter_location.loc[data["GeoLocation"]!="(0.000000, 0.000000)"]

# We only want meteors that fell after 1906
filter_dates = filter_location.loc[filter_location["year"] >= 1906]
filter_dates = filter_dates.loc[filter_dates["year"] <= 2013]

# Remove Geoloc since we have Lat/Lng
meteors = filter_dates[["name","id","nametype","recclass","mass","fall","year","reclat","reclong"]]

# Make empty lists to add to so we can add them to the dataframe
cities = []
countries = []

# Loop through the dataframe
for index, row in meteors.iterrows():
    # Grab Lat and Lng to use in functions
    lat = row["reclat"]
    lng = row["reclong"]
    # Find the closest city to the coordinates and append it to the cities list
    city = citipy.nearest_city(lat, lng).city_name
    cities.append(city)
    # Find which meteorites landed in North America
    if lng > -180 and lng < -60 and lat > 25 and lat < 75:
        countries.append("North America")
    else:
        countries.append("Drop")

# Add the cities and countries to the dataframe
meteors["city"] = cities   
meteors["country"] = countries

# Drop everything that isn't North America and write it to a csv
clean_df = meteors.loc[meteors["country"] == "North America", :]
clean_df.to_csv("Resources/clean_meteorites.csv")