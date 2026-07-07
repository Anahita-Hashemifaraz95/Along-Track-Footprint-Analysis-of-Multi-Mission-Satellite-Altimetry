from reader import read_cycle
from distance import compute_distance

import pandas as pd


def run(data_path, tracks, missions):

    for mission in missions:

        print("\n==========================")
        print(f"Mission: {mission}")
        print("==========================")

        mission_segments = []

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

                # خواندن فایل
                df = read_cycle(cycle_file)

                if df.empty:
                    print(f"  Empty: {cycle_file.name}")
                    continue

                # محاسبه فاصله بین نقاط متوالی
                segments = compute_distance(df)

                if segments.empty:
                    print(f"  Not enough points: {cycle_file.name}")
                    continue

                # افزودن شماره گذر
                segments["track"] = track

                # ذخیره خروجی این Cycle
                mission_segments.append(segments)

                print(
                    f"  {cycle_file.name} -> "
                    f"{len(df)} points, "
                    f"{len(segments)} segments"
                )

        # =====================================
        # تجمیع همه Segmentهای این Mission
        # =====================================

        if not mission_segments:
            print(f"\nNo valid data for {mission}")
            continue

        mission_df = pd.concat(
            mission_segments,
            ignore_index=True,
        )

        print(f"\nMission {mission} completed.")
        print(f"Total segments: {len(mission_df)}")

        # در مرحله بعد این DataFrame
        # به تابع تشخیص داده‌های پرت ارسال می‌شود.