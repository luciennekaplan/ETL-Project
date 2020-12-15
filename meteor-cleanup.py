import pandas as pd
from citipy import citipy
import os
from uszipcode import SearchEngine
from uszipcode import Zipcode

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

search = SearchEngine(simple_zipcode=True)
# Make empty lists to add to so we can add them to the dataframe
cities = []
state = []
ziplist = []
# Loop through the dataframe
for index, row in meteors.iterrows():
    # Grab Lat and Lng to use in functions
    lat = row["reclat"]
    lng = row["reclong"]
    # Find the closest city to the coordinates and append it to the cities list
    city = citipy.nearest_city(lat, lng).city_name
    cities.append(city)
    # Find which meteorites landed in North America
    try:
        result = search.by_coordinates(lat, lng, radius=25, returns=1)
        zipcode = result[0].zipcode
        st = result[0].state
        ziplist.append(zipcode)
        state.append(st)
    except IndexError:
        ziplist.append("Drop")
        state.append("Drop")

# Add the cities and countries to the dataframe
meteors["city"] = cities   
meteors["zipcode"] = ziplist
meteors["state"] = state
# Drop everything that isn't North America and write it to a csv
clean_df = meteors.loc[meteors["zipcode"] != "Drop", :]
clean_df.to_csv("Resources/clean_meteorites.csv", index = False)