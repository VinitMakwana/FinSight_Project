"""
Exploratory Data Analysis
FinSight Credit Risk Analytics
"""

import warnings

warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import ttest_ind
from scipy.stats import pearsonr

from pathlib import Path

sns.set_style("whitegrid")

FIGURE_DIR = Path(
    "reports/eda/figures"
)

# Load the dataset
df = pd.read_parquet(
    "data/processed/clean_dataset.parquet"
)

print(df.shape)

# Q2(a)
# Loan Status Distribution
#Bar chart
def loan_status_bar_chart(df):

    plt.figure(
        figsize=(8, 5)
    )

    sns.countplot(
        data=df,
        x="loan_status"
    )

    plt.title(
        "Loan Status Distribution"
    )

    plt.xlabel(
        "Loan Status"
    )

    plt.ylabel(
        "Count"
    )

    plt.tight_layout()

    plt.savefig(
        FIGURE_DIR /
        "loan_status_bar.png"
    )

    plt.show()

# Pie chart
def loan_status_pie_chart(df):

    status_counts = (
        df["loan_status"]
        .value_counts()
    )

    plt.figure(
        figsize=(7, 7)
    )

    plt.pie(
        status_counts,
        labels=status_counts.index,
        autopct="%1.2f%%"
    )

    plt.title(
        "Loan Status Distribution"
    )

    plt.savefig(
        FIGURE_DIR /
        "loan_status_pie.png"
    )

    plt.show()

# Default Rate
def calculate_default_rate(df):

    default_rate = (
        df["loan_status"]
        .mean()
        * 100
    )

    print(
        f"Default Rate: "
        f"{default_rate:.2f}%"
    )

    return default_rate

# Q2(b)
# CIBIL KDE Analysis
# Cohen's D
def cohens_d(
    group1,
    group2
):

    pooled_std = np.sqrt(
        (
            (
                group1.std() ** 2
            )
            +
            (
                group2.std() ** 2
            )
        ) / 2
    )

    d = (
        group1.mean()
        -
        group2.mean()
    ) / pooled_std

    return d

# KDE Plot
def cibil_kde_analysis(df):

    defaulted = (
        df[
            df.loan_status == 1
        ]["cibil_score"]
    )

    performing = (
        df[
            df.loan_status == 0
        ]["cibil_score"]
    )

    plt.figure(
        figsize=(10, 6)
    )

    sns.kdeplot(
        defaulted,
        label="Defaulted"
    )

    sns.kdeplot(
        performing,
        label="Performing"
    )

    plt.title(
        "CIBIL Score Distribution"
    )

    plt.xlabel(
        "CIBIL Score"
    )

    plt.legend()

    plt.savefig(
        FIGURE_DIR /
        "cibil_kde.png"
    )

    plt.show()

    print(
        "Default Mean:",
        defaulted.mean()
    )

    print(
        "Performing Mean:",
        performing.mean()
    )

    print(
        "Cohen's D:",
        round(
            cohens_d(
                defaulted,
                performing
            ),
            3
        )
    )

# Q2(c)
# 12 Panel Histogram
def histogram_grid(df):

    numeric_cols = (
        df
        .select_dtypes(
            include=np.number
        )
        .columns[:12]
    )

    fig, axes = plt.subplots(
        3,
        4,
        figsize=(18, 12)
    )

    axes = axes.flatten()

    for i, col in enumerate(
        numeric_cols
    ):

        sns.histplot(
            df[col],
            kde=True,
            ax=axes[i]
        )

        axes[i].set_title(
            col
        )

    plt.tight_layout()

    plt.savefig(
        FIGURE_DIR /
        "histogram_grid.png"
    )

    plt.show()

# Q2(d)
# Coorelation Heatmap
def correlation_heatmap(df):

    numeric_df = (
        df.select_dtypes(
            include=np.number
        )
    )

    corr_matrix = (
        numeric_df
        .corr()
    )

    top_features = (
        corr_matrix
        .abs()
        .sum()
        .sort_values(
            ascending=False
        )
        .head(20)
        .index
    )

    plt.figure(
        figsize=(14, 10)
    )

    sns.heatmap(
        corr_matrix.loc[
            top_features,
            top_features
        ],
        annot=True,
        fmt=".2f",
        cmap="coolwarm"
    )

    plt.title(
        "Correlation Heatmap"
    )

    plt.tight_layout()

    plt.savefig(
        FIGURE_DIR /
        "correlation_heatmap.png"
    )

    plt.show()

# Q2(e)
# Box Plots
def boxplot_analysis(df):

    features = [
        "int_rate_pct",
        "dti_pct",
        "cibil_score",
        "annual_inc_inr",
        "revol_util_pct",
        "emp_length_years"
    ]

    fig, axes = plt.subplots(
        2,
        3,
        figsize=(18, 10)
    )

    axes = axes.flatten()

    for idx, feature in enumerate(
        features
    ):

        sns.boxplot(
            data=df,
            x="loan_status",
            y=feature,
            ax=axes[idx]
        )

        axes[idx].set_title(
            feature
        )

    plt.tight_layout()

    plt.savefig(
        FIGURE_DIR /
        "boxplots.png"
    )

    plt.show()

# Q2(f)
# Default Rate by Grade
def grade_default_rate(df):

    grade_rate = (
        df.groupby("grade")
        ["loan_status"]
        .mean()
        .sort_index()
        * 100
    )

    grade_rate.plot(
        kind="bar",
        figsize=(10, 5)
    )

    plt.title(
        "Default Rate by Grade"
    )

    plt.ylabel(
        "Default Rate (%)"
    )

    plt.tight_layout()

    plt.savefig(
        FIGURE_DIR /
        "grade_default_rate.png"
    )

    plt.show()

    return grade_rate

# Q2(g)
# Loan Purpose Analysis
def purpose_default_rate(df):

    purpose_rate = (
        df.groupby("primary_enq_purpose")
        ["loan_status"]
        .mean()
        * 100
    )

    purpose_rate = (
        purpose_rate
        .sort_values(
            ascending=False
        )
    )

    purpose_rate.plot(
        kind="barh",
        figsize=(12, 8)
    )

    plt.title(
        "Default Rate by Purpose"
    )

    plt.tight_layout()

    plt.savefig(
        FIGURE_DIR /
        "purpose_default_rate.png"
    )

    plt.show()

    purpose_rate.to_csv(
        "reports/eda/purpose_risk_report.csv"
    )

    return purpose_rate

# Q2(h)
# State Risk Analysis
def state_default_rate(df):

    state_rate = (
        df.groupby("state_code")
        ["loan_status"]
        .mean()
        * 100
    )

    state_rate = (
        state_rate
        .sort_values(
            ascending=False
        )
        .head(10)
    )

    state_rate.plot(
        kind="bar",
        figsize=(12, 6)
    )

    plt.title(
        "Top 10 Risk States"
    )

    plt.ylabel(
        "Default Rate (%)"
    )

    plt.tight_layout()

    plt.savefig(
        FIGURE_DIR /
        "state_default_rate.png"
    )

    plt.show()

    state_rate.to_csv(
        "reports/eda/state_risk_report.csv"
    )

    return state_rate

# Q2(i)
# Annual Default Trend
def annual_default_trend(df):

    yearly = (
        df.groupby(
            "issue_year"
        )["loan_status"]
        .mean()
        * 100
    )

    yearly.plot(
        marker="o",
        figsize=(12, 5)
    )

    plt.title(
        "Annual Default Rate"
    )

    plt.ylabel(
        "Default Rate (%)"
    )

    plt.tight_layout()

    plt.savefig(
        FIGURE_DIR /
        "annual_default_trend.png"
    )

    plt.show()

    return yearly

# Q2(j)
# Repo Rate vs Default Rate
def repo_rate_analysis(df):

    annual = (
        df.groupby(
            "issue_year"
        )
        .agg(
            {
                "loan_status": "mean",
                "rbi_repo_rate_pct": "mean"
            }
        )
    )

    fig, ax1 = plt.subplots(
        figsize=(12, 6)
    )

    ax2 = ax1.twinx()

    ax1.plot(
        annual.index,
        annual.loan_status * 100,
        marker="o"
    )

    ax2.plot(
        annual.index,
        annual.rbi_repo_rate_pct,
        marker="s"
    )

    ax1.set_ylabel(
        "Default Rate (%)"
    )

    ax2.set_ylabel(
        "Repo Rate"
    )

    plt.title(
        "Repo Rate vs Default Rate"
    )

    plt.savefig(
        FIGURE_DIR /
        "repo_rate_vs_default.png"
    )

    plt.show()

# Q2(k)
def lgd_distribution(df):

    lgd_df = (
        df[
            df.loan_status == 1
        ]
    )

    plt.figure(
        figsize=(10, 6)
    )

    sns.histplot(
        lgd_df["lgd_pct"],
        kde=True
    )

    plt.title(
        "LGD Distribution"
    )

    plt.savefig(
        FIGURE_DIR /
        "lgd_distribution.png"
    )

    plt.show()

# Q2(l)
# CIBIL vs LGD
def cibil_vs_lgd(df):

    lgd_df = (
        df[
            df.loan_status == 1
        ]
    )

    plt.figure(
        figsize=(10, 6)
    )

    sns.regplot(
        data=lgd_df,
        x="cibil_score",
        y="lgd_pct"
    )

    plt.title(
        "CIBIL Score vs LGD"
    )

    plt.savefig(
        FIGURE_DIR /
        "cibil_vs_lgd.png"
    )

    plt.show()

    r, p = pearsonr(
        lgd_df["cibil_score"],
        lgd_df["lgd_pct"]
    )

    print(
        f"Pearson r = {r:.3f}"
    )

    print(
        f"P-value = {p:.6f}"
    )