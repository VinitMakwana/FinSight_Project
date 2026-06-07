from src.data_ingestion import DataIngestion

pipeline = DataIngestion()

summary = pipeline.run()

print(summary.head())