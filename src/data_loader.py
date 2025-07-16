import pandas as pd
from src.utils import extract_genres

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath, low_memory=False, usecols=['title', 'genres', 'runtime', 'original_language'])
    df['genres'] = df['genres'].apply(extract_genres)
    df = df.dropna()
    df = df[df['runtime'].astype(float).between(30, 240)]
    df.reset_index(drop=True, inplace=True)
    return df
