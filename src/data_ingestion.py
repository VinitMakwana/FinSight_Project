"""
Data Ingestion Module

FinSight Bank Credit Risk Analytics
"""

from pathlib import Path
import pandas as pd
import numpy as np

from src.config import (
    RAW_DATA_DIR,
    PARQUET_DATA_DIR,
    CHUNK_SIZE,
    PRIMARY_KEY
)


class DataIngestion:
    """
    Data ingestion pipeline.
    """

    def __init__(self):

        self.raw_path = RAW_DATA_DIR

        self.parquet_path = PARQUET_DATA_DIR

    @staticmethod
    def memory_usage_mb(df):

        return round(
            df.memory_usage(deep=True).sum() /
            (1024 ** 2),
            2
        )

    @staticmethod
    def optimize_dtypes(df):
        """
        Downcast numeric columns.
        """

        for col in df.select_dtypes(
            include=["int"]
        ).columns:

            df[col] = pd.to_numeric(
                df[col],
                downcast="integer"
            )

        for col in df.select_dtypes(
            include=["float"]
        ).columns:

            df[col] = pd.to_numeric(
                df[col],
                downcast="float"
            )

        return df

    def read_large_csv(
        self,
        file_path
    ):
        """
        Read large csv using chunks.
        """

        chunks = []

        for chunk in pd.read_csv(
            file_path,
            chunksize=CHUNK_SIZE,
            low_memory=False
        ):

            chunks.append(chunk)

        return pd.concat(
            chunks,
            ignore_index=True
        )

    def validate_primary_key(
        self,
        df,
        file_name
    ):
        """
        Check loan_id existence.
        """

        if PRIMARY_KEY not in df.columns:

            raise ValueError(
                f"{PRIMARY_KEY} missing in {file_name}"
            )

    def save_parquet(
        self,
        df,
        file_name
    ):

        parquet_file = (
            self.parquet_path /
            f"{file_name}.parquet"
        )

        df.to_parquet(
            parquet_file,
            index=False,
            engine="pyarrow"
        )

        return parquet_file

    def process_file(
        self,
        file_path
    ):

        print(f"\nProcessing: {file_path.name}")

        df = self.read_large_csv(
            file_path
        )

        self.validate_primary_key(
            df,
            file_path.name
        )

        memory_before = self.memory_usage_mb(
            df
        )

        df = self.optimize_dtypes(df)

        memory_after = self.memory_usage_mb(
            df
        )

        parquet_file = self.save_parquet(
            df,
            file_path.stem
        )

        result = {
            "file_name": file_path.name,
            "rows": len(df),
            "columns": len(df.columns),
            "memory_before_mb": memory_before,
            "memory_after_mb": memory_after,
            "parquet_file": str(parquet_file)
        }

        return result

    def run(self):

        csv_files = list(
            self.raw_path.glob("*.csv")
        )

        if len(csv_files) == 0:

            raise FileNotFoundError(
                "No CSV files found."
            )

        ingestion_summary = []

        for file in csv_files:

            result = self.process_file(
                file
            )

            ingestion_summary.append(
                result
            )

        summary_df = pd.DataFrame(
            ingestion_summary
        )

        summary_df.to_csv(
            "data/metadata/ingestion_summary.csv",
            index=False
        )

        print(
            "\nData Ingestion Completed"
        )

        return summary_df