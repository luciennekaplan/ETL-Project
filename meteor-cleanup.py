import pandas as pd
import os

# Import the raw CSV
path = os.path.join(os.path.dirname(__file__),"meteorite-landings.csv")
data = pd.read_csv(path)
print(data.count())

# Filter out the invalid locations
filter_location = data.dropna()
filter_location = filter_location.loc[data["GeoLocation"]!="(0.000000, 0.000000)"]
print(filter_location.count())

# We only want meteors that fell after 1906
filter_dates = filter_location.loc[filter_location["year"] > 1906]
print(filter_dates.count())
