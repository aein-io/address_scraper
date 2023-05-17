import os

import folium
import pandas as pd
from geopy.geocoders import Nominatim


def map(filename: str, logger) -> None:
    """
    Display the output addresses to a map.

    Args:
        filename (str): Name of the csv file to map.

    Returns:
        None: Displays a map in the browser.

    """

    df = pd.read_csv(filename)
    geolocator = Nominatim(user_agent="my_map")

    map_obj = folium.Map()

    # Iterate over the addresses in the DataFrame
    failed_coords = 0
    for _, row in df.iterrows():
        latitude = row["lat"]
        longitude = row["lon"]
        if latitude == 0 or longitude == 0:
            logger(
                f"Invalid coordinates: {row['street_name']}, {latitude}, {longitude}")
            failed_coords += 1
            continue

        coords = f"{latitude}, {longitude}"

        location = geolocator.reverse(coords)
        address = location.address  # type: ignore

        folium.Marker(
            location=[location.latitude, location.longitude],  # type: ignore
            popup=address,
        ).add_to(map_obj)

    logger(f"Failed to get coordinates for {failed_coords} addresses.")
    map_obj.save("map.html")
    os.system("open map.html")
