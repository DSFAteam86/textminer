from number_reader import *
from config import path
from order_frame import *

list_name = "NITS"

data = find_numbers_with(
    path=path,
    search_terms=["NIT"],
    value_name=list_name,
    left_offset=0,
    right_offset=20
)


def found_nits(data):

    possible_nits = []
    for document in data:
        consecutive_numbers = []
        for text in document[list_name]:
            consecutive_numbers.append(get_consecutives(text))

        possible_nits.append({
            "uid": document["uid"],
            list_name: consecutive_numbers
        })

    return possible_nits


found_nits = found_nits(data)
no_duplicates_with_verifiers = remove_duplicates(found_nits, list_name)

nits_without_verifiers = trim_data(
    data=no_duplicates_with_verifiers,
    list_name=list_name,
    end=9
)

nits_without_duplicates = remove_duplicates(nits_without_verifiers, list_name)


def get_error_nits(nit):
    nitLength = len(nit)
    if(nitLength < 9 and nitLength > 0):
        return nit


def get_empty_nits(nit):
    nitLength = len(nit)
    if(nitLength == 0):
        return nit


def get_possible_nits(nit):
    nitLength = len(nit)
    if(nitLength == 9):
        return nit


error_nits = run_over_list(nits_without_duplicates, get_error_nits, list_name)
empty_nits = run_over_list(nits_without_duplicates, get_empty_nits, list_name)
possible_nits = run_over_list(
    nits_without_duplicates, get_possible_nits, list_name)


df_error_nits_ungrouped = dataframe_from_dict(error_nits, list_name)
df_empty_nits_ungrouped = dataframe_from_dict(empty_nits, list_name)
df_possible_nits_ungrouped = dataframe_from_dict(possible_nits, list_name)


print("df_error_nits_ungrouped: ")
print(df_error_nits_ungrouped, "\n")

print("df_empty_nits_ungrouped: ")
print(df_empty_nits_ungrouped, "\n")

print("df_possible_nits_ungrouped: ")
print(df_possible_nits_ungrouped)
