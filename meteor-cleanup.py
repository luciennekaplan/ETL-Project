import pandas as pd
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

# Remove lat/long since we have GeoLoc
meteors = filter_dates[["name","id","nametype","recclass","mass","fall","year","GeoLocation"]]
print(meteors.head())