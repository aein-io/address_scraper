import os
import sys
import pandas as pd
from geopy.geocoders import Nominatim
import folium

csv_files = [file for file in os.listdir() if file.endswith('.csv')]
if len(csv_files) > 0:
    csv_file = csv_files[0]
else:
    sys.exit("No CSV files found in the current directory.")

df = pd.read_csv(csv_file)

geolocator = Nominatim(user_agent='my_map')

map_obj = folium.Map()

# Iterate over the addresses in the DataFrame
for index, row in df.iterrows():

    latitude = row['lat']
    longitude = row['lon']
    if latitude == 0 or longitude == 0:
        continue

    coords = f"{latitude}, {longitude}"

    location = geolocator.reverse(coords)
    address = location.address

    folium.Marker(
        location=[location.latitude, location.longitude],
        popup=address
    ).add_to(map_obj)

# Display the map
map_obj.save('map.html')
# open the map
os.system('open map.html')
