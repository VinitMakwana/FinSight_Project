'''
Utility Functions
'''

import pandas as pd

def memory_usage_mb(df:pd.DataFrame) -> float:
    return round(df.memory_usage(index=True).sum() / 1024 ** 2, 2)

def dataframe_shape(df:pd.DataFrame) -> tuple:
    return df.shape