import pandas as pd


def load_advertising_data(filepath):
    """
    Load advertising dataset from CSV file.
    """
    return pd.read_csv(filepath)


