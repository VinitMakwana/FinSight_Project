import pandas as pd

from src.data_cleaning import (
    clean_dataset
)

df = pd.read_parquet(
    "data/processed/master_dataset.parquet"
)

clean_df = clean_dataset(df)

clean_df.to_parquet(
    "data/processed/"
    "clean_dataset.parquet",
    index=False
)

print(
    "Clean Dataset Saved"
)