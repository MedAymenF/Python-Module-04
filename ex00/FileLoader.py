import pandas as pd


class FileLoader:
    @staticmethod
    def load(path):
        try:
            df = pd.read_csv(path)
        except Exception as e:
            print(e)
            return None
        else:
            print('Loading dataset of dimensions {} x {}'.format(*df.shape))
            return df

    @staticmethod
    def display(df, n):
        if not isinstance(n, int):
            return None
        try:
            if n > 0:
                print(df.head(n))
            else:
                print(df.tail(-n))
        except Exception as e:
            print(e)
