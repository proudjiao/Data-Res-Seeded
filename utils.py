import pandas as pd

def drop_invalid(df, relevant_columns):
  new_df = df[relevant_columns].copy()
  return new_df.dropna()
