from pathlib import Path


def run(data_path, tracks, missions):

    for mission in missions:

        print("\n==========================")
        print(f"Mission: {mission}")
        print("==========================")

        for track in tracks:

            pass_folder = data_path / f"Pass-{track:03d}"
            mission_folder = pass_folder / mission

            if not mission_folder.exists():
                print(f"Missing: {mission_folder}")
                continue

            print(f"\nPass: {track}")

            cycle_files = sorted(
                mission_folder.glob("cycle_*.txt")
            )

            if not cycle_files:
                print("  No cycle files found")
                continue

            for cycle_file in cycle_files:
                print(f"  {cycle_file.name}")