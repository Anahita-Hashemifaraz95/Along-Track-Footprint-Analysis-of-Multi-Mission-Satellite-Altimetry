from pathlib import Path

from project1 import run


DATA_PATH = Path(r"C:\Users\surface\Desktop\project1\data")
OUTPUT_PATH = Path(r"C:\Users\surface\Desktop\project1")

TRACKS = [
    16,
    31,
    57,
    92,
    107,
    133,
    168,
    209,
    244,
]


MISSIONS = [
    "TOPEX-POSEIDON",
    "JASON-1",
    "JASON-2",
    "JASON-3",
]


run(
    data_path=DATA_PATH,
    output_path=OUTPUT_PATH,
    tracks=TRACKS,
    missions=MISSIONS,
)