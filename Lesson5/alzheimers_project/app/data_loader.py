import pandas as pd
from .config import DATA_FILE

def load_data():
    try:
        df = pd.read_csv(DATA_FILE)
        return df
    except FileNotFoundError:
        print("Помилка: файл з даними не знайдено.")
        return None