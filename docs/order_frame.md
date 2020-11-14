# order_frame

This file will serve as documentation for [order_frame.py](../order_frame.py)

### remove_unwanted_chars(column, chars)

Removes characters from a column

Params:

- **column**: Takes a dataframe column or a Series
- **chars**: the characters you want to remove from every row in a column

### create_ungrouped_dataframe(df, lst_col)

If a dataframe has a column that contains an array of values, this function will spread those values and assign them an independant row. Example

input DataFrame

| reference | value      |
| --------- | ---------- |
| 1         | [123, 456] |
| 2         | [3, 4]     |

output:

| reference | value |
| --------- | ----- |
| 1         | 123   |
| 1         | 456   |
| 2         | 3     |
| 2         | 4     |

Params:

- **df**: DataFrame with array column
- **lst_col**: name of the column

### dataframe_from_dict(dict_data, list_name)

Creates a dataframe from a dictionary with uid column and a column with array values

- **dict_data**: Dictionary with uids and array
- **list_name**: Since this function uses create_ungrouped_dataframe it needs a column name
