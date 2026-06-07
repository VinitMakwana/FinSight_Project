'''
Project configuration file
FinSight Bank Credit Risk Analytics
'''

from pathlib import Path

# Project root
PROJECT_ROOT = Path.cwd()

# Data Directories

RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
INTERIM_DATA_DIR = PROJECT_ROOT / "data" / "interim"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"
PARQUET_DATA_DIR = PROJECT_ROOT / "data" / "parquet"
METADATA_DIR = PROJECT_ROOT / "data" / "metadata"


# Reports
REPORT_DIR = PROJECT_ROOT / "reports"
EDA_REPORT_DIR = REPORT_DIR / "eda"
MODEL_REPORT_DIR = REPORT_DIR / "model_results"
BUSINESS_REPORT_DIR = REPORT_DIR / "business_reports"


# Logs
LOG_DIR = PROJECT_ROOT / "logs"

# Models
MODEL_DIR = PROJECT_ROOT / "models"

# Random state
RANDOM_STATE = 42

# Target Variables
REGRESSION_TARGET = "lgd_pct"

CHUNK_SIZE = 100_000

PRIMARY_KEY = "loan_id"