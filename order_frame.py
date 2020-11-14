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


def dataframe_from_dict(dict_data, list_name):
    if(len(dict_data) > 0):
        df_type_name = pd.DataFrame.from_dict(dict_data)
        df_type_name["uid"] = remove_unwanted_chars(
            df_type_name["uid"], ".txt")

        df = create_ungrouped_dataframe(df_type_name, list_name)
        return df
    else:
        return "Empty DataFrame (no occurrences were found)"
