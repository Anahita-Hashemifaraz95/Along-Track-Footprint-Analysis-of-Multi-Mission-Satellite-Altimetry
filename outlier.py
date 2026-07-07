import pandas as pd


def detect_outliers_stepwise(df, steps=4):
    """
    Stepwise 3-sigma outlier detection.

    Parameters
    ----------
    df : pandas.DataFrame

    steps : int
        Number of sigma-removal iterations.

    Returns
    -------
    list[pandas.DataFrame]
        [step1, step2, ..., remaining]
    """

    remaining = df.copy()

    groups = []

    for _ in range(steps):

        if remaining.empty:
            groups.append(pd.DataFrame(columns=df.columns))
            continue

        mean = remaining["distance"].mean()
        std = remaining["distance"].std()

        lower = mean - 3 * std
        upper = mean + 3 * std

        mask = (
            (remaining["distance"] < lower)
            | (remaining["distance"] > upper)
        )

        outliers = remaining.loc[mask].copy()

        groups.append(outliers)

        remaining = remaining.loc[~mask].copy()

    groups.append(remaining)

    return groups

def distance_statistics(groups):
    """
    Compute distance statistics for each outlier group.
    """

    names = [
        "Step 1",
        "Step 2",
        "Step 3",
        "Step 4",
        "Remaining",
    ]

    rows = []

    for name, group in zip(names, groups):

        if group.empty:

            rows.append({
                "Group": name,
                "Count": 0,
                "Mean": None,
                "Std": None,
                "Min": None,
                "Max": None,
                "Median": None,
            })

            continue

        distance = group["distance"]

        rows.append({
            "Group": name,
            "Count": len(distance),
            "Mean": distance.mean(),
            "Std": distance.std(),
            "Min": distance.min(),
            "Max": distance.max(),
            "Median": distance.median(),
        })

    return pd.DataFrame(rows)

def save_statistics(stats, mission, output_path):

    """

    Save distance statistics table.

    Parameters

    ----------

    stats : pandas.DataFrame

    mission : str

    output_path : pathlib.Path

    """

    output_path.mkdir(

        parents=True,

        exist_ok=True,

    )

    file_name = f"{mission}_statistics.csv"

    stats.to_csv(

        output_path / file_name,

        index=False,

        float_format="%.3f",

    )