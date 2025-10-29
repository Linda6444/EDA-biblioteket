import pandas as pd

def total_loans(df: pd.DataFrame) -> int:
    return df["book_title"].nunique()

def avg_loan_days(df: pd.DataFrame) -> float:
    return float(df["loan_duration_days"].mean())
