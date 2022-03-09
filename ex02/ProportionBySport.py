def proportionBySport(df, year, sport, gender):
    total_df = df[(df['Year'] == year) & (df['Sex'] == gender)]
    total = len(total_df.drop_duplicates(subset='ID'))
    df_by_sport = total_df[total_df['Sport'] == sport]
    numerator = len(df_by_sport.drop_duplicates(subset='ID'))
    return numerator / total
