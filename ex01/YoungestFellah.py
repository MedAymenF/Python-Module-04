import pandas as pd


def youngfellah(df, year):
    """Get the name of the youngest woman and man for the given year.
Args:
        df: pandas.DataFrame object containing the dataset.
        year: integer corresponding to a year.
Returns:
        dct: dictionary with 2 keys for female and male athlete."""
    if not isinstance(df, pd.DataFrame) or not isinstance(year, int):
        return None
    dct = {}
    df_by_year = df[df['Year'] == year]
    dct['f'] = df_by_year[df_by_year['Sex'] == 'F']['Age'].min()
    dct['m'] = df_by_year[df_by_year['Sex'] == 'M']['Age'].min()
    return dct
