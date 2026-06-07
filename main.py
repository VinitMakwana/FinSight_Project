'''
Main Project
'''

from src.logger import get_logger
logger = get_logger(__name__)

def main():
    logger.info('FinSight Credit Risk Project Started')
    print('FinSight Bank Credit Risk Analytics')
    logger.info('Project Intialized Successfully')

if __name__ == '__main__':
    main()

'''
Project Setup Script
'''
from pathlib import Path

folders =[
"data/interim",
    "data/processed",
    "data/parquet",
    "reports/eda",
    "reports/model_results",
    "reports/business_reports",
    "models",
    "notebooks",
    "tests"
]

for folder in folders:
    Path(folder).mkdir(parents=True, exist_ok=True)

print('Project Structure Created Successfully')

'''
Validation Script
'''

required_folders = [
    "data",
    "logs",
    "models",
    "src",
    "notebooks"
]

for folder in required_folders:

    if Path(folder).exists():
        print(f"✓ {folder} exists")
    else:
        print(f"✗ {folder} missing")

print("\nValidation Complete")