def pandas_append_inplace(df, row):
    df.loc[-1] = row
    df.index = df.index + 1
    df = df.sort_index()
