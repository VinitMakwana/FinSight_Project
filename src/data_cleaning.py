"""
FinSight Data Cleaning Pipeline
"""

from pathlib import Path

import numpy as np
import pandas as pd

from scipy.stats.mstats import winsorize

# Step 1: Creating Data cleaning Module

class DataCleaner:

    def __init__(self):

        self.cleaning_log = []

    def log_issue(
        self,
        issue_name,
        count
    ):

        self.cleaning_log.append(
            {
                "issue_name": issue_name,
                "count": count
            }
        )

    def generate_cleaning_report(self):

        report = pd.DataFrame(
            self.cleaning_log
        )

        report.to_csv(
            "data/metadata/cleaning_report.csv",
            index=False
        )

        return report

# Step 2: Creating Dirty Flag
def create_dirty_flag(df):

    dirty_flag = pd.Series(
        False,
        index=df.index
    )

    # CIBIL

    dirty_flag |= (
        (df["cibil_score"] < 300)
        |
        (df["cibil_score"] > 900)
    )

    # Income

    dirty_flag |= (
        df["annual_inc_inr"] <= 0
    )

    # Interest Rate

    dirty_flag |= (
        (df["int_rate_pct"] <= 0)
        |
        (df["int_rate_pct"] > 100)
    )

    # DTI

    dirty_flag |= (
        (df["dti_pct"] < 0)
        |
        (df["dti_pct"] > 200)
    )

    # Employment Years

    dirty_flag |= (
        df["emp_length_years"] < 0
    )

    df["dirty_flag"] = (
        dirty_flag.astype(int)
    )

    return df

# Missing Target Handling
def remove_missing_targets(df):

    before_rows = len(df)

    df = df.dropna(
        subset=[
            "loan_status",
            "lgd_pct"
        ]
    )

    removed_rows = (
        before_rows - len(df)
    )

    print(
        f"Removed {removed_rows} rows "
        f"with missing targets"
    )

    return df

# Step 4: Missing Value Audit
def missing_value_report(df):

    report = pd.DataFrame(
        {
            "missing_count":
                df.isnull().sum(),

            "missing_percent":
                round(
                    (
                        df.isnull().mean()
                        * 100
                    ),
                    2
                )
        }
    )

    report = report.sort_values(
        "missing_percent",
        ascending=False
    )

    report.to_csv(
        "reports/cleaning/"
        "missing_value_report.csv"
    )

    return report

# Step 5: Missing value Treatment
# 1. mrot_acc
def impute_mort_acc(df):

    median_value = (
        df["mort_acc"]
        .median()
    )

    df["mort_acc"] = (
        df["mort_acc"]
        .fillna(median_value)
    )

    return df

# 2. emp_length_years
def impute_emp_length(df):

    median_value = (
        df["emp_length_years"]
        .median()
    )

    df["emp_length_years"] = (
        df["emp_length_years"]
        .fillna(median_value)
    )

    return df

# 3. mths_since_last_delinq
def impute_last_delinq(df):

    df[
        "mths_since_last_delinq"
    ] = (
        df[
            "mths_since_last_delinq"
        ]
        .fillna(999)
    )

    return df

# 4. il_util_pct
def impute_il_util(df):

    median_value = (
        df["il_util_pct"]
        .median()
    )

    df["il_util_pct"] = (
        df["il_util_pct"]
        .fillna(median_value)
    )

    return df

# Step 6: Domain Corrections
def fix_cibil(df):

    invalid_count = len(
        df[
            (df["cibil_score"] < 300)
            |
            (df["cibil_score"] > 900)
        ]
    )

    df.loc[
        df["cibil_score"] < 300,
        "cibil_score"
    ] = 300

    df.loc[
        df["cibil_score"] > 900,
        "cibil_score"
    ] = 900

    print(
        f"Fixed {invalid_count} "
        "CIBIL values"
    )

    return df

# Annual Income
def fix_income(df):

    median_income = (
        df.loc[
            df["annual_inc_inr"] > 0,
            "annual_inc_inr"
        ]
        .median()
    )

    df.loc[
        df["annual_inc_inr"] <= 0,
        "annual_inc_inr"
    ] = median_income

    return df

# DTI
def fix_dti(df):

    median_dti = (
        df[
            (df["dti_pct"] >= 0)
            &
            (df["dti_pct"] <= 200)
        ]["dti_pct"]
        .median()
    )

    df.loc[
        (df["dti_pct"] < 0)
        |
        (df["dti_pct"] > 200),
        "dti_pct"
    ] = median_dti

    return df

# Step 7: Winsorization
def winsorize_column(
    df,
    column
):

    before_mean = df[column].mean()

    before_std = df[column].std()

    before_max = df[column].max()

    df[column] = winsorize(
        df[column],
        limits=[0.01, 0.01]
    )

    after_mean = df[column].mean()

    after_std = df[column].std()

    after_max = df[column].max()

    return {
        "column": column,

        "before_mean": before_mean,

        "after_mean": after_mean,

        "before_std": before_std,

        "after_std": after_std,

        "before_max": before_max,

        "after_max": after_max
    }

# Step 8: Apply winsorization to top 6 skewed columns
def winsorization_pipeline(
    df
):

    numeric_cols = (
        df
        .select_dtypes(
            include=np.number
        )
        .columns
    )

    skewness = (
        df[numeric_cols]
        .skew()
        .abs()
        .sort_values(
            ascending=False
        )
    )

    top_6 = (
        skewness.head(6).index
    )

    results = []

    for col in top_6:

        result = winsorize_column(
            df,
            col
        )

        results.append(result)

    report = pd.DataFrame(
        results
    )

    report.to_csv(
        "reports/cleaning/"
        "winsorization_report.csv",
        index=False
    )

    return df

# Step 9: Full Cleaning Pipeline
def clean_dataset(df):

    print(
        "Starting Cleaning..."
    )

    df = create_dirty_flag(df)

    df = remove_missing_targets(df)

    df = impute_mort_acc(df)

    df = impute_emp_length(df)

    df = impute_last_delinq(df)

    df = impute_il_util(df)

    df = fix_cibil(df)

    df = fix_income(df)

    df = fix_dti(df)

    df = winsorization_pipeline(df)

    return df