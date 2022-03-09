import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.api.types import is_numeric_dtype


class Komparator:
    def __init__(self, df):
        if not isinstance(df, pd.DataFrame):
            raise ValueError
        self.df = df

    def compare_box_plots(self, categorical_var, numerical_var):
        if categorical_var not in self.df or numerical_var not in self.df:
            print("Column doesn't exist")
            return None
        if not is_numeric_dtype(self.df[numerical_var]):
            print('Not a numerical variable')
            return None
        sns.boxplot(x=self.df[categorical_var], y=self.df[numerical_var])
        plt.show()

    def density(self, categorical_var, numerical_var):
        if categorical_var not in self.df or numerical_var not in self.df:
            print("Column doesn't exist")
            return None
        if not is_numeric_dtype(self.df[numerical_var]):
            print('Not a numerical variable')
            return None
        sns.kdeplot(data=self.df, x=numerical_var, hue=categorical_var)
        plt.show()

    def compare_histograms(self, categorical_var, numerical_var):
        if categorical_var not in self.df or numerical_var not in self.df:
            print("Column doesn't exist")
            return None
        if not is_numeric_dtype(self.df[numerical_var]):
            print('Not a numerical variable')
        sns.histplot(data=self.df, x=numerical_var, hue=categorical_var)
        plt.show()
