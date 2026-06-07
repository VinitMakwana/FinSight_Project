"""
FinSight Data Integration Pipeline

Creates master_dataset.parquet
"""

from pathlib import Path

import pandas as pd

from src.config import PARQUET_DATA_DIR

PRIMARY_KEY = "loan_id"
EXPECTED_ROWS = 2_000_000


class DataIntegrator:

    def __init__(self):

        self.parquet_path = PARQUET_DATA_DIR

    def load_parquet(self, file_name):

        file_path = (
            self.parquet_path /
            f"{file_name}.parquet"
        )

        return pd.read_parquet(file_path)

    def validate_rows(self, df, step):

        current_rows = len(df)

        print(
            f"{step} : {current_rows:,} rows"
        )

        assert current_rows == EXPECTED_ROWS, (
            f"Row count mismatch after {step}"
        )

    def orphan_records(self,
                       left_df,
                       right_df):

        orphan_count = (
            ~right_df[PRIMARY_KEY]
            .isin(left_df[PRIMARY_KEY])
        ).sum()

        return orphan_count

    def merge_tables(self):

        # Base table

        master_df = self.load_parquet(
            "loans_master"
        )

        self.validate_rows(
            master_df,
            "Base Table"
        )

        tables = [
            "branch_region_economy",
            "collateral_assets",
            "credit_card_behavior",
            "customer_bureau",
            "loan_enquiry_bureau",
            "loan_performance",
            "monthly_emi_track",
            "payment_history"
        ]

        for table in tables:

            right_df = self.load_parquet(
                table
            )

            orphan_count = (
                self.orphan_records(
                    master_df,
                    right_df
                )
            )

            print(
                f"{table} Orphans: "
                f"{orphan_count:,}"
            )

            master_df = master_df.merge(
                right_df,
                how="left",
                on=PRIMARY_KEY
            )

            self.validate_rows(
                master_df,
                table
            )

        return master_df

    def save_master_dataset(
        self,
        df
    ):

        output_path = (
            Path("data/processed")
            /
            "master_dataset.parquet"
        )

        df.to_parquet(
            output_path,
            index=False,
            engine="pyarrow"
        )

        print(
            f"\nSaved -> {output_path}"
        )

        return output_path

from src.data_integration import (
    DataIntegrator
)

integrator = DataIntegrator()

master_df = (
    integrator.merge_tables()
)

integrator.save_master_dataset(
    master_df
)

print(
    master_df.shape
)