#!/usr/bin/env python3
"""
NTU Assignment - Pandas (Correlation, Reshape, Datetime Slicing)

Run:
    python assignment_pandas.py
"""

import pandas as pd
import numpy as np


def q1_correlation() -> float:
    returns = pd.DataFrame({
        "MSFT": [0.05, 0.07, -0.01],
        "IBM":  [0.04, 0.02, 0.03],
    })
    corr_msft_ibm = returns["MSFT"].corr(returns["IBM"])
    return corr_msft_ibm


def q2_wide_to_long() -> pd.DataFrame:
    df = pd.DataFrame({
        "A": {0: "a", 1: "b", 2: "c"},
        "B": {0: 1,   1: 3,   2: 5},
        "C": {0: 2,   1: 4,   2: 6},
    })
    df_long = df.melt(id_vars="A", value_vars=["B", "C"], var_name="variable", value_name="value")
    return df_long


def q3_slice_series() -> pd.Series:
    dates = pd.date_range("2023-01-01", "2023-01-31")
    data = pd.Series(np.random.rand(len(dates)), index=dates)
    slice_data = data.loc["2023-01-05":"2023-01-15"]
    return slice_data


def main() -> None:
    print("=" * 70)
    print("Q1: Correlation (MSFT vs IBM)")
    print("=" * 70)
    print(q1_correlation())

    print("\n" + "=" * 70)
    print("Q2: Wide to Long (melt B & C)")
    print("=" * 70)
    print(q2_wide_to_long())

    print("\n" + "=" * 70)
    print("Q3: Slice Series (2023-01-05 to 2023-01-15)")
    print("=" * 70)
    print(q3_slice_series())


if __name__ == "__main__":
    main()
