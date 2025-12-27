import pandas as pd
from .config import DATA_FILE

def load_data(path=DATA_FILE) -> pd.DataFrame:
    """
    Lädt die Kreditdaten aus CSV.
    """
    return pd.read_csv(path)
