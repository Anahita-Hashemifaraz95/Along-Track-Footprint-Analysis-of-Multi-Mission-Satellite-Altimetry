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