import pandas as pd

from src.eda import *

df = pd.read_parquet(
    "data/processed/clean_dataset.parquet"
)

loan_status_bar_chart(df)

loan_status_pie_chart(df)

calculate_default_rate(df)

cibil_kde_analysis(df)

histogram_grid(df)

correlation_heatmap(df)

boxplot_analysis(df)

grade_default_rate(df)

purpose_default_rate(df)

state_default_rate(df)

annual_default_trend(df)

repo_rate_analysis(df)

lgd_distribution(df)

cibil_vs_lgd(df)

print(
    "EDA Completed Successfully"
)