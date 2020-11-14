import pandas as pd
import numpy as np


def remove_unwanted_chars(column, chars):
    return column.map(lambda x: x.lstrip('+-').rstrip(chars))


def create_ungrouped_dataframe(df, lst_col):
    r = pd.DataFrame({
        col: np.repeat(df[col].values, df[lst_col].str.len())
        for col in df.columns.drop(lst_col)}
    ).assign(**{lst_col: np.concatenate(df[lst_col].values)})[df.columns]
    return r


def dataframe_from_dict(df_name):
    df_type_name = pd.DataFrame.from_dict(df_name)
    df_type_name["uid"] = remove_unwanted_chars(df_type_name["uid"], ".txt")
    return df_type_name
