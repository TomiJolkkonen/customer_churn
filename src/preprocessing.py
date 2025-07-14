import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess(df):
    df = df.dropna()
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        df[col] = LabelEncoder().fit_transform(df[col])
    return df
