import pandas as pd
import numpy as np


def howManyMedals(df, name):
    if not isinstance(df, pd.DataFrame) or not isinstance(name, str):
        return None
    df = df[df['Name'] == name]
    df = df.replace({'Medal': {'Gold': 'G', 'Silver': 'S', 'Bronze': 'B'}})
    df = df.groupby(['Year', 'Medal'], dropna=False).size()
    df = df.unstack(fill_value=0)
    if np.nan in df:
        df = df.drop(np.nan, axis=1)
    cols = ['G', 'S', 'B']
    df = df.reindex(df.columns.union(cols, sort=False), axis=1, fill_value=0)
    dct = df.to_dict(orient='index')
    return dct
