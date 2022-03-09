import pandas as pd
from pandas.api.types import is_numeric_dtype
import matplotlib.pyplot as plt
import seaborn as sns


class MyPlotLib:
    def histogram(self, data, features):
        if not isinstance(data, pd.DataFrame)\
                or not isinstance(features, list):
            return None
        features = list(filter(lambda x: is_numeric_dtype(data[x]), features))
        data[features].hist()
        plt.show()

    def density(self, data, features):
        if not isinstance(data, pd.DataFrame)\
                or not isinstance(features, list):
            return None
        data[features].plot.kde()
        plt.show()

    def pair_plot(self, data, features):
        if not isinstance(data, pd.DataFrame)\
                or not isinstance(features, list):
            return None
        sns.pairplot(data[features], diag_kind='hist',
                     diag_kws=dict(bins=10), plot_kws=dict(s=7))
        plt.show()

    def box_plot(self, data, features):
        if not isinstance(data, pd.DataFrame)\
                or not isinstance(features, list):
            return None
        features = list(filter(lambda x: is_numeric_dtype(data[x]), features))
        data.boxplot(column=features)
        plt.show()
