import pandas as pd

REQUIRED = [
    "book_title", "category", "branch",
    "loan_date", "return_date", "loan_duration_days"
]

def load_data(path: str) -> pd.DataFrame:
    # talar om vad funktionen gör när man hovrar
    """
    läser CSV och gör kolumner till datetime 
    """
    df = pd.read_csv(path, parse_dates=["loan_date", "return_date"])

    missing = [c for c in REQUIRED if c not in df.columns]
    if missing:
        raise ValueError(f"Saknade kolumner: {missing}")
    return df

def coerce_numeric(df: pd.DataFrame) -> pd.DataFrame:
    """
    säkerställer att numeriska kolumner är numeriska
    """

    out = df.copy()
    for c in ["loan_date", "return_date", "loan_duration_days"]:
        out[c] = pd.to_numeric(out[c], errors="coerce")
        return out

