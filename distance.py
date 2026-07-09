import numpy as np
import pandas as pd


EARTH_RADIUS_KM = 6371.0


def compute_distance(df):
    """
    Compute distance between consecutive observations.
    """

    if len(df) < 2:
        return pd.DataFrame(
            columns=[
                "distance",
                "Latitude",
                "Longitude",
                "time",
            ]
        )

    lat = df["Latitude"].to_numpy()
    lon = df["Longitude"].to_numpy()
    time = df["time"].to_numpy()

    # Coordinate difference
    dlat = np.radians(lat[1:] - lat[:-1])
    dlon = np.radians(lon[1:] - lon[:-1])

    lat1 = np.radians(lat[:-1])
    lat2 = np.radians(lat[1:])

    # Haversine Formula
    a = (
        np.sin(dlat / 2) ** 2
        + np.cos(lat1)
        * np.cos(lat2)
        * np.sin(dlon / 2) ** 2
    )

    distance = (
        2
        * EARTH_RADIUS_KM
        * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    )

    return pd.DataFrame(
        {
            "distance": distance,
            "Latitude": (lat[:-1] + lat[1:]) / 2,
            "Longitude": (lon[:-1] + lon[1:]) / 2,
            "time": time[:-1],
        }
    )
