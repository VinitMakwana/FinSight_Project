# 💳 FinSight — Bank Credit Risk Analytics & Data Engineering

> **Turning raw banking data into reliable credit-risk insights through a structured, quality-first data pipeline.**

FinSight is an end-to-end **Bank Credit Risk Analytics and Data Engineering project** designed to transform raw financial data into clean, validated, analysis-ready datasets and actionable risk insights.

The project focuses on the complete data lifecycle — from **data ingestion and integration to cleaning, validation, data-quality assessment, exploratory data analysis (EDA), and analytical reporting**.

The architecture is designed with a modular approach so that individual stages of the pipeline can be maintained, tested, and extended independently.

---

## 📌 Project Overview

Financial institutions deal with large volumes of borrower, loan, repayment, credit-score, collateral, and economic data.

Raw financial datasets often contain:

- Missing values
- Duplicate records
- Invalid values
- Inconsistent formats
- Data-type issues
- Outliers
- Referential inconsistencies

These issues can significantly affect downstream credit-risk analysis.

**FinSight** addresses this problem by implementing a structured data pipeline that prepares financial data for reliable analytics.

### Core Pipeline

```text
                    ┌─────────────────────┐
                    │   Raw Financial     │
                    │       Data          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Data Ingestion    │
                    │   & Integration     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Data Cleaning     │
                    │  & Transformation   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Data Validation   │
                    │   & Quality Checks   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Clean Parquet      │
                    │      Dataset        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       EDA           │
                    │  Risk & Trend       │
                    │     Analysis        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Reports & Business  │
                    │      Insights       │
                    └─────────────────────┘
```

---

# ✨ Key Features

## 🔹 1. Data Ingestion

The ingestion layer is responsible for bringing raw financial data into the project pipeline.

It provides the foundation for downstream processing and ensures that datasets enter the system in a controlled manner.

---

## 🔹 2. Data Cleaning

FinSight includes a dedicated data-cleaning layer for preparing raw data for analytics.

Typical processing includes:

- Missing-value handling
- Duplicate detection
- Data-type standardization
- Invalid-value handling
- Column normalization
- Data transformation
- Outlier preparation
- Dataset consistency checks

The cleaning pipeline generates an analysis-ready dataset in **Parquet format**.

---

## 🔹 3. Data Quality Framework

A dedicated data-quality module evaluates the cleaned dataset across multiple dimensions:

### Completeness

Measures whether required fields contain valid data.

### Validity

Checks whether values conform to expected rules and ranges.

### Uniqueness

Identifies duplicate or non-unique records.

### Consistency

Checks whether related fields and values remain logically consistent.

### Quality Scorecard

The project combines these checks into a **data-quality scorecard** that provides a high-level view of dataset quality.

The quality pipeline generates reports such as:

```text
reports/
└── data_quality/
    ├── completeness_report.csv
    ├── validity_report.csv
    ├── uniqueness_report.csv
    ├── consistency_report.csv
    └── quality_scorecard.csv
```

The repository's data-quality runner reads the cleaned Parquet dataset and generates these individual reports and the final scorecard.

---

# 📊 Exploratory Data Analysis

FinSight provides a dedicated EDA layer for understanding borrower and loan-risk patterns.

The analysis includes:

### Credit Risk Analysis

- Loan status distribution
- Default-rate analysis
- Credit-score analysis
- Grade-wise default rate
- Loan-purpose default rate
- State-wise default rate
- Annual default trends

### Financial Analysis

- LGD distribution
- CIBIL/credit-score vs. LGD analysis
- Interest/economic indicator analysis
- Repo-rate analysis

### Statistical Analysis

- Distribution analysis
- Correlation analysis
- KDE plots
- Histograms
- Boxplots
- Correlation heatmaps

The EDA runner currently executes analyses including loan-status charts, default-rate calculations, CIBIL KDE analysis, correlation heatmaps, grade/purpose/state default rates, annual default trends, repo-rate analysis, LGD distribution, and CIBIL-vs-LGD analysis.

---

# 🏗️ Project Architecture

```text
FinSight_Project/
│
├── data/
│   ├── raw/
│   ├── interim/
│   ├── processed/
│   └── parquet/
│
├── logs/
│
├── models/
│
├── notebooks/
│   └── report.ipynb
│
├── reports/
│   ├── eda/
│   ├── model_results/
│   ├── business_reports/
│   └── data_quality/
│
├── src/
│   ├── config.py
│   ├── data_ingestion.py
│   ├── data_cleaning.py
│   ├── data_integration.py
│   ├── data_quality.py
│   ├── data_validation.py
│   ├── eda.py
│   ├── logger.py
│   ├── metadata_logger.py
│   └── utils.py
│
├── main.py
├── run_ingestion.py
├── run_cleaning.py
├── run_data_quality.py
├── run_eda.py
├── requirements.txt
└── README.md
```

The repository currently contains dedicated modules for ingestion, cleaning, integration, data quality, validation, EDA, logging, metadata logging, and utilities.

---

# 🧩 Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Data Analysis | SciPy, Statsmodels |
| Machine Learning | Scikit-learn |
| Visualization | Matplotlib, Seaborn |
| Data Storage | Parquet |
| Parquet Engines | PyArrow, FastParquet |
| Database / Integration | SQLAlchemy |
| Excel Processing | OpenPyXL |
| Notebook Environment | Jupyter Notebook |
| Model Utilities | Joblib |
| Logging | Python-based custom logging |
| Version Control | Git & GitHub |

---

# 🔄 End-to-End Workflow

## Step 1 — Data Ingestion

```text
Raw Data
   ↓
Data Ingestion
   ↓
Initial Dataset
```

The ingestion layer brings the source data into the project.

---

## Step 2 — Data Cleaning

```text
Initial Dataset
      ↓
Missing Values
      ↓
Duplicates
      ↓
Invalid Records
      ↓
Type Standardization
      ↓
Clean Dataset
```

The resulting dataset is stored as:

```text
data/processed/clean_dataset.parquet
```

---

## Step 3 — Data Quality

```text
Clean Dataset
      │
      ├── Completeness
      │
      ├── Validity
      │
      ├── Uniqueness
      │
      └── Consistency
             │
             ▼
      Quality Scorecard
```

---

## Step 4 — Exploratory Data Analysis

```text
Clean Dataset
      │
      ├── Default Analysis
      ├── Credit Score Analysis
      ├── Loan Grade Analysis
      ├── Purpose Analysis
      ├── Geographic Analysis
      ├── Economic Analysis
      └── LGD Analysis
             │
             ▼
        Visual Reports
```

---

# 🚀 Getting Started

## Prerequisites

Make sure the following are installed:

- Python 3.9+
- Git
- Jupyter Notebook

Verify Python:

```bash
python --version
```

Verify Git:

```bash
git --version
```

---

# 📥 Installation

### 1. Clone the repository

```bash
git clone https://github.com/VinitMakwana/FinSight_Project.git
```

### 2. Navigate to the project

```bash
cd FinSight_Project
```

### 3. Create a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

The repository pins versions for its core data-science dependencies, including Pandas 2.2.2, NumPy 1.26.4, Scikit-learn 1.5.0, PyArrow 16.1.0, SQLAlchemy 2.0.30 and others.

---

# ▶️ Running the Project

## Run the Main Project

```bash
python main.py
```

The main entry point initializes the FinSight project and logging framework.

---

## Run Data Ingestion

```bash
python run_ingestion.py
```

---

## Run Data Cleaning

```bash
python run_cleaning.py
```

---

## Run Data Quality Analysis

```bash
python run_data_quality.py
```

This generates:

```text
reports/data_quality/
```

with completeness, validity, uniqueness, consistency, and quality-scorecard reports.

---

## Run Exploratory Data Analysis

```bash
python run_eda.py
```

This executes the project's financial-risk EDA functions and generates the corresponding analysis outputs.

---

# 📁 Data Layers

FinSight follows a layered data organization approach:

```text
data/
│
├── raw/
│       Raw source datasets
│
├── interim/
│       Intermediate processing results
│
├── processed/
│       Clean and validated datasets
│
└── parquet/
        Columnar analytical storage
```

This separation helps maintain traceability between source data, transformed data, and analytical datasets.

---

# 📈 Business Insights

FinSight is designed to answer questions such as:

### Credit Risk

- What percentage of loans are defaulting?
- Which loan grades have higher default rates?
- Which loan purposes show greater credit risk?
- How does credit score affect default behavior?
- Which states demonstrate higher default rates?

### Loss Analysis

- What is the distribution of Loss Given Default (LGD)?
- How does credit quality relate to LGD?
- Which borrower segments experience higher expected losses?

### Economic Factors

- How do economic indicators relate to credit risk?
- How does repo-rate movement relate to default trends?
- How do default rates change over time?

---

# 🧠 Data Engineering Concepts Demonstrated

This project demonstrates practical implementation of:

- ETL / ELT concepts
- Data ingestion
- Data cleaning
- Data transformation
- Data validation
- Data quality engineering
- Data integration
- Columnar storage with Parquet
- Exploratory data analysis
- Statistical analysis
- Data profiling
- Logging
- Metadata management
- Modular Python architecture
- Reproducible analytical workflows

---

# 📊 Data Quality Philosophy

A key design principle of FinSight is:

> **Reliable analytics starts with reliable data.**

Instead of directly performing analysis on raw financial data, the project introduces explicit validation and quality stages.

```text
                 Raw Data
                    │
                    ▼
              Data Cleaning
                    │
                    ▼
             Data Validation
                    │
                    ▼
             Data Quality
                    │
                    ▼
             Analysis Dataset
                    │
                    ▼
              Risk Analytics
```

This approach reduces the possibility of incorrect business conclusions caused by poor-quality input data.

---

# 🛠️ Project Design Principles

### Modular Architecture

Each major processing responsibility is separated into its own Python module.

### Reusability

Common operations are organized into reusable functions rather than being duplicated across scripts.

### Traceability

Different data stages and generated reports are stored separately.

### Quality First

Data-quality checks are performed before analytical processing.

### Analytical Reproducibility

EDA and processing can be executed through dedicated scripts.

---

# 📚 Notebook

The repository also contains:

```text
notebooks/report.ipynb
```

The notebook can be used for interactive exploration, analysis, visualization, and documenting findings.

---

# 🔮 Future Enhancements

The project can be extended into a production-grade credit-risk platform by adding:

### 🤖 Machine Learning

- Default prediction
- Probability of Default (PD)
- Loss Given Default (LGD) prediction
- Expected Loss (EL) estimation
- Logistic Regression
- Random Forest
- XGBoost / LightGBM
- Model comparison
- Hyperparameter tuning

### 🏦 Credit Risk Metrics

```text
Expected Loss = PD × LGD × EAD
```

Where:

- **PD** → Probability of Default
- **LGD** → Loss Given Default
- **EAD** → Exposure at Default

### ⚡ Big Data

Future versions can integrate:

- Apache Spark
- Hadoop HDFS
- Apache Kafka
- Spark Structured Streaming
- Delta Lake

### ☁️ Cloud

Potential deployment architecture:

```text
Data Sources
     ↓
Kafka / API
     ↓
Spark
     ↓
Cloud Object Storage
     ↓
Data Warehouse / Lakehouse
     ↓
ML Models
     ↓
Risk Dashboard
```

Possible cloud platforms include:

- AWS
- Microsoft Azure
- Google Cloud

### 📊 Dashboard

A production dashboard could provide:

- Portfolio risk overview
- Default-rate KPIs
- PD/LGD/EL metrics
- Borrower segmentation
- Geographic risk maps
- Loan-grade risk
- Trend analysis
- Model predictions

---

# 🔐 Data & Security

This project is intended for **educational, analytical, and portfolio purposes**.

Do not commit:

```text
.env
credentials
API keys
private financial information
personally identifiable information
production database credentials
```

Sensitive configuration should be stored outside source control.

---

# 👨‍💻 Author

### Vinit Makwana

GitHub:  
https://github.com/VinitMakwana

Repository:  
https://github.com/VinitMakwana/FinSight_Project

---

# ⭐ If You Find This Project Useful

If FinSight helps you understand data engineering and credit-risk analytics:

- ⭐ Star the repository
- 🍴 Fork the project
- 🐛 Open an issue
- 💡 Suggest improvements
- 🤝 Contribute to the project

---

## 📜 License

This project is currently intended as an educational/portfolio project.

Add an explicit license file if you want others to legally reuse, modify, or distribute the code.

---

## 📌 Project Summary

**FinSight** demonstrates how a financial dataset can be transformed into a reliable analytical asset through a structured data-engineering workflow:

```text
                FIN SIGHT
                    │
                    ▼
          ┌──────────────────┐
          │  Data Ingestion  │
          └────────┬─────────┘
                   ▼
          ┌──────────────────┐
          │ Data Integration │
          └────────┬─────────┘
                   ▼
          ┌──────────────────┐
          │ Data Cleaning    │
          └────────┬─────────┘
                   ▼
          ┌──────────────────┐
          │ Data Validation  │
          └────────┬─────────┘
                   ▼
          ┌──────────────────┐
          │ Data Quality     │
          └────────┬─────────┘
                   ▼
          ┌──────────────────┐
          │ Parquet Dataset  │
          └────────┬─────────┘
                   ▼
          ┌──────────────────┐
          │      EDA         │
          └────────┬─────────┘
                   ▼
          ┌──────────────────┐
          │ Risk Insights    │
          └──────────────────┘
```

> **FinSight — Engineering reliable financial data for smarter credit-risk analytics.**
