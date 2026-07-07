from reader import read_cycle
from distance import compute_distance


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

                # خواندن فایل
                df = read_cycle(cycle_file)

                if df.empty:
                    print(f"  Empty: {cycle_file.name}")
                    continue

                # محاسبه فاصله
                segments = compute_distance(df)

                if segments.empty:
                    print(f"  Not enough points: {cycle_file.name}")
                    continue

                # افزودن شماره گذر
                segments["track"] = track

                # ذخیره نتایج
                mission_data.append(segments)

                print(
                    f"  {cycle_file.name} -> "
                    f"{len(df)} points, "
                    f"{len(segments)} segments"
                )

        print(f"\nMission {mission} completed.")

        # -----------------------------
        # مرحله بعد
        # -----------------------------
        #
        # mission_df = pd.concat(
        #     mission_data,
        #     ignore_index=True
        # )
        #
        # detect_outliers(mission_df)
        #
        # statistics(mission_df)
        #
        # plots(mission_df)