import pandas as pd

from src.data_quality import *

df = pd.read_parquet(
    "data/processed/clean_dataset.parquet"
)

completeness = (
    completeness_report(df)
)

validity = (
    validity_report(df)
)

uniqueness = (
    uniqueness_report(df)
)

consistency = (
    consistency_report(df)
)

scorecard = (
    generate_quality_scorecard(df)
)

completeness.to_csv(
    "reports/data_quality/completeness_report.csv",
    index=False
)

validity.to_csv(
    "reports/data_quality/validity_report.csv",
    index=False
)

uniqueness.to_csv(
    "reports/data_quality/uniqueness_report.csv",
    index=False
)

consistency.to_csv(
    "reports/data_quality/consistency_report.csv",
    index=False
)

scorecard.to_csv(
    "reports/data_quality/quality_scorecard.csv",
    index=False
)

print(scorecard)