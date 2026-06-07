"""
Metadata Logging
"""

from datetime import datetime
import pandas as pd


def log_metadata(
    file_name,
    rows,
    columns
):

    metadata = pd.DataFrame(
        {
            "file_name": [file_name],
            "rows": [rows],
            "columns": [columns],
            "timestamp": [datetime.now()]
        }
    )

    metadata.to_csv(
        "data/metadata/load_log.csv",
        mode="a",
        header=False,
        index=False
    )