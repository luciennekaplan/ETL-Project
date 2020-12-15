# First we'll import the os module
# This will allow us to create file paths across operating systems

import pandas as pd
from uszipcode import SearchEngine
from uszipcode import Zipcode
file = "Resources/complete.csv"

UFO_df = pd.read_csv(file,  error_bad_lines=False)


UFOs_in_US = UFO_df[UFO_df['country'] == 'us']

cleanUSUFO = UFOs_in_US.loc[UFOs_in_US['datetime'] != '10/10/2005 24:00' ]

yeartime = UFOs_in_US['datetime'].str.split(pat='/', expand=True)

year = yeartime[2].str.split(pat=' ', expand=True)

UFOs_in_US['Year']= year[0]

UFOs_in_US['datetime'].drop

year_UFOs_in_US = UFOs_in_US[['city', 'state', 'country', 'shape', 'duration (hours/min)', 'comments', 'latitude', 'longitude', 'Year']]

search = SearchEngine(simple_zipcode=True)
ziplist = []
for index, row in year_UFOs_in_US.iterrows():
    # Grab Lat and Lng to use in functions
    lat = round(float(row["latitude"]), 5)
    lng = round(row["longitude"], 5)
    try:
        result = search.by_coordinates(lat, lng, radius=25, returns=1)
        zipcode = result[0].zipcode
        ziplist.append(zipcode)
    except IndexError:
        ziplist.append("Drop")

year_UFOs_in_US["zipcode"] = ziplist

year_UFOs_in_US = year_UFOs_in_US.loc[year_UFOs_in_US["zipcode"] != "Drop", :]

final_UFO = year_UFOs_in_US[(year_UFOs_in_US['Year']>='1906') | (year_UFOs_in_US['Year'] <= '2013')]

final_UFO.to_csv(r'Resources\final_UFO.csv')