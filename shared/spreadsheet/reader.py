import pandas as pd

def read_spreadsheet(file_path, column):
    """Reads a spreadsheet and return a specific column as a list."""
    df = pd.read_excel(file_path)
    return df[column].tolist()
