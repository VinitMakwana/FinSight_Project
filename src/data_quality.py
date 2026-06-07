"""
Data Quality Assessment
"""

import pandas as pd
import numpy as np

# Completeness assesment
def completeness_score(df):

    total_cells = (
        df.shape[0]
        * df.shape[1]
    )

    missing_cells = (
        df.isnull()
        .sum()
        .sum()
    )

    score = (
        (
            total_cells
            - missing_cells
        )
        /
        total_cells
    ) * 100

    return round(
        score,
        2
    )

# Column level completeness
def completeness_report(df):

    report = pd.DataFrame(
        {
            "column":
            df.columns,

            "missing_count":
            df.isnull().sum(),

            "completeness_pct":
            (
                100
                -
                (
                    df.isnull()
                    .mean()
                    * 100
                )
            ).round(2)
        }
    )

    return report

# Validity assesment
def validity_report(df):

    results = []

    cibil_invalid = len(
        df[
            (df["cibil_score"] < 300)
            |
            (df["cibil_score"] > 900)
        ]
    )

    results.append(
        [
            "cibil_score",
            cibil_invalid
        ]
    )

    income_invalid = len(
        df[
            df["annual_inc_inr"] <= 0
        ]
    )

    results.append(
        [
            "annual_inc_inr",
            income_invalid
        ]
    )

    dti_invalid = len(
        df[
            (df["dti_pct"] < 0)
            |
            (df["dti_pct"] > 200)
        ]
    )

    results.append(
        [
            "dti_pct",
            dti_invalid
        ]
    )

    report = pd.DataFrame(
        results,
        columns=[
            "column",
            "invalid_records"
        ]
    )

    return report

# Uniqueness assessment
def uniqueness_report(df):

    duplicate_count = (
        df["loan_id"]
        .duplicated()
        .sum()
    )

    report = pd.DataFrame(
        {
            "metric":
            ["duplicate_loan_id"],

            "count":
            [duplicate_count]
        }
    )

    return report

# Consistency assessment
def consistency_report(df):

    consistency_results = []

    if (
        "collateral_value_inr"
        in df.columns
    ):

        invalid_collateral = len(
            df[
                df[
                    "collateral_value_inr"
                ]
                <
                df[
                    "loan_amnt_inr"
                ]
            ]
        )

        consistency_results.append(
            [
                "collateral_less_than_loan",
                invalid_collateral
            ]
        )

    report = pd.DataFrame(
        consistency_results,
        columns=[
            "rule",
            "violations"
        ]
    )

    return report

# Data quality scorecard
def generate_quality_scorecard(df):

    completeness = (
        completeness_score(df)
    )

    duplicate_pct = (
        df["loan_id"]
        .duplicated()
        .mean()
        * 100
    )

    uniqueness = (
        100 - duplicate_pct
    )

    overall_score = (
        completeness
        +
        uniqueness
    ) / 2

    scorecard = pd.DataFrame(
        {
            "metric":
            [
                "completeness",
                "uniqueness",
                "overall_score"
            ],

            "score":
            [
                completeness,
                uniqueness,
                overall_score
            ]
        }
    )

    return scorecard

# Visualization
import matplotlib.pyplot as plt

def quality_dashboard(scorecard):

    plt.figure(
        figsize=(8, 5)
    )

    plt.bar(
        scorecard["metric"],
        scorecard["score"]
    )

    plt.title(
        "Data Quality Scorecard"
    )

    plt.ylabel(
        "Score (%)"
    )

    plt.show()