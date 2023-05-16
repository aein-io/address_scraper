import os
import pandas as pd
from geopy.geocoders import Nominatim
import folium

# Find the first CSV file in the current directory
csv_files = [file for file in os.listdir() if file.endswith('.csv')]
if len(csv_files) > 0:
    csv_file = csv_files[0]
else:
    print('No CSV files found in the current directory.')
    exit()

# Read addresses from the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file)

# Initialize the geocoder
geolocator = Nominatim(user_agent='my_map')

# Create a map object
map_obj = folium.Map()

# Iterate over the addresses in the DataFrame
for index, row in df.iterrows():

    address = f"{row['city']}, {row['state']}, {row['street_name']}, {row['street_number']}, {row['lat']}, {row['lon']}"

    # Use geocoder to get the latitude and longitude of the address
    location = geolocator.geocode(address)

    # Add a marker to the map
    folium.Marker(
        location=[location.latitude, location.longitude],
        popup=address
    ).add_to(map_obj)

# Display the map
map_obj.save('map.html')
