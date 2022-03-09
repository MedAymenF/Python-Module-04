import pandas as pd


class SpatioTemporalData:
    def __init__(self, df):
        if not isinstance(df, pd.DataFrame):
            raise ValueError
        self.df = df

    def when(self, location):
        return self.df[self.df['City'] == location]['Year'].unique()

    def where(self, date):
        return self.df[self.df['Year'] == date]['City'].unique()
