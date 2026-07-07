from pathlib import Path

from reader import read_cycle


def run(data_path, tracks, missions):

    for mission in missions:

        print("\n==========================")
        print(f"Mission: {mission}")
        print("==========================")

        mission_data = []

        for track in tracks:

            pass_folder = data_path / f"Pass_{track:03d}"
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

                df = read_cycle(cycle_file)

                if df.empty:
                    print(f"  Empty: {cycle_file.name}")
                    continue

                print(f"  {cycle_file.name}  ({len(df)} points)")

                # Next Step:
                # segments = compute_distance(df)
                # segments["track"] = track
                # mission_data.append(segments)

        print(f"\nMission {mission} completed.")