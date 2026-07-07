# reader.py

import pandas as pd

COLUMNS = [
    "Latitude",
    "Longitude",
    "SSH",
    "time",
]


def read_cycle(file_path):
    """
    Read one cycle text file.

    Parameters
    ----------
    file_path : pathlib.Path

    Returns
    -------
    pandas.DataFrame
    """

    try:
        return pd.read_csv(
            file_path,
            sep=r"\s+",
            header=None,
            names=COLUMNS,
        )

    except pd.errors.EmptyDataError:
        return pd.DataFrame(columns=COLUMNS)