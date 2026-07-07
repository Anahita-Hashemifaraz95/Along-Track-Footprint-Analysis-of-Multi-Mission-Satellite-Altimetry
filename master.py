from pathlib import Path

from project1 import run


DATA_PATH = Path(r"C:\Users\surface\Desktop\project1\data")


TRACKS = [
    16,
    133,
]


MISSIONS = [
    "TOPEX-POSEIDON",
    "JASON-1",
    "JASON-2",
    "JASON-3",
]


run(
    data_path=DATA_PATH,
    tracks=TRACKS,
    missions=MISSIONS,
)