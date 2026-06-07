"""
Data Validation Module
"""

from pathlib import Path
import pandas as pd


class DataValidator:

    def __init__(self):

        self.validation_results = []

    def add_result(
        self,
        check_name,
        status,
        count
    ):

        self.validation_results.append(
            {
                "check_name": check_name,
                "status": status,
                "count": count
            }
        )

    def validate_primary_key(
        self,
        df
    ):

        missing_pk = (
            df["loan_id"]
            .isnull()
            .sum()
        )

        duplicate_pk = (
            df["loan_id"]
            .duplicated()
            .sum()
        )

        self.add_result(
            "missing_primary_key",
            "PASS" if missing_pk == 0 else "FAIL",
            missing_pk
        )

        self.add_result(
            "duplicate_primary_key",
            "PASS" if duplicate_pk == 0 else "FAIL",
            duplicate_pk
        )

    def validate_row_count(
        self,
        df,
        expected_rows
    ):

        status = (
            "PASS"
            if len(df) == expected_rows
            else "FAIL"
        )

        self.add_result(
            "row_count_check",
            status,
            len(df)
        )

    def generate_report(self):

        report = pd.DataFrame(
            self.validation_results
        )

        report.to_csv(
            "reports/validation_report.csv",
            index=False
        )

        return report

def missing_value_audit(df):

    audit = pd.DataFrame(
        {
            "missing_count":
            df.isnull().sum(),

            "missing_percent":
            (
                df.isnull().mean() * 100
            ).round(2)
        }
    )

    audit = (
        audit
        .sort_values(
            "missing_percent",
            ascending=False
        )
    )

    return audit

def domain_validation(df):

    validation_summary = {}

    validation_summary[
        "invalid_cibil"
    ] = len(
        df[
            (df["cibil_score"] < 300)
            |
            (df["cibil_score"] > 900)
        ]
    )

    validation_summary[
        "invalid_income"
    ] = len(
        df[
            df["annual_inc"] <= 0
        ]
    )

    validation_summary[
        "invalid_dti"
    ] = len(
        df[
            (df["dti"] < 0)
            |
            (df["dti"] > 200)
        ]
    )

    return validation_summary

def validate_targets(df):

    target_report = {}

    target_report[
        "loan_status_missing"
    ] = (
        df["loan_status"]
        .isnull()
        .sum()
    )

    target_report[
        "lgd_missing"
    ] = (
        df["lgd_pct"]
        .isnull()
        .sum()
    )

    return target_report

import pandas as pd

from src.data_validation import (
    DataValidator
)

df = pd.read_parquet(
    "data/processed/master_dataset.parquet"
)

validator = DataValidator()

validator.validate_primary_key(
    df
)

validator.validate_row_count(
    df,
    expected_rows=2_000_000
)

report = (
    validator
    .generate_report()
)

print(report)