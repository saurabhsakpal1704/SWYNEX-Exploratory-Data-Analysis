from pathlib import Path
import re
import numpy as np
import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "processed" / "adult_cleaned.csv"

def normalize_columns(df):
    df = df.copy()
    original = list(df.columns)
    new = []
    for c in df.columns:
        c = str(c).strip().lower()
        c = re.sub(r"[^a-z0-9]+", "_", c).strip("_")
        new.append(c)
    df.columns = new
    return df, dict(zip(original, new))

def find_col(columns, candidates):
    cols = list(columns)
    for candidate in candidates:
        if candidate in cols:
            return candidate
    for col in cols:
        if any(candidate in col for candidate in candidates):
            return col
    return None

def load_data(path=DATA_PATH):
    if not path.exists():
        raise FileNotFoundError(
            f"Dataset not found at {path}. Put your Task 1 cleaned file there "
            "and name it adult_cleaned.csv."
        )
    df = pd.read_csv(path)
    df, mapping = normalize_columns(df)
    return df, mapping

def detect_columns(df):
    return {
        "target": find_col(df.columns, ["income", "income_class", "income_level", "salary", "target"]),
        "age": find_col(df.columns, ["age"]),
        "education": find_col(df.columns, ["education", "education_num", "educational"]),
        "occupation": find_col(df.columns, ["occupation"]),
        "workclass": find_col(df.columns, ["workclass"]),
        "hours": find_col(df.columns, ["hours_per_week", "hours"]),
        "capital_gain": find_col(df.columns, ["capital_gain"]),
        "sex": find_col(df.columns, ["sex", "gender"]),
    }

if __name__ == "__main__":
    df, mapping = load_data()
    cols = detect_columns(df)
    print("Shape:", df.shape)
    print("Columns:", list(df.columns))
    print("\nDetected columns:")
    for k, v in cols.items():
        print(f"{k}: {v}")
    print("\nMissing values:")
    print(df.isna().sum().sort_values(ascending=False).head(20))
    print("\nDuplicate rows:", df.duplicated().sum())
