from number_reader import *
from config import path
from order_frame import *

list_name = "CEDULAS"

data = find_numbers_with(
    path=path,
    search_terms=[
        "cedula de ciudadanía",
        "cédula de ciudadanía",
        "cedula de ciudadania",
        "cédula de ciudadania",
        "CEDULA DE CIUDADANIA",
        "CÉDULA DE CIUDADANÍA",
        "CÉDULA DE CIUDADANIA",
        "CEDULA DE CIUDADANÍA",
        "C\.C\.",
        "C\. C\."],
    value_name=list_name,
    left_offset=0,
    right_offset=50
)


def found_cedulas(data):

    possible_cc = []
    for document in data:
        consecutive_numbers = []
        for text in document[list_name]:
            consecutive_numbers.append(get_consecutives(text))

        possible_cc.append({
            "uid": document["uid"],
            list_name: consecutive_numbers
        })

    return possible_cc


possible_cc = found_cedulas(data)
cc_without_duplicates = remove_duplicates(possible_cc, list_name)


def trim_cedula_length(cedula):
    return cedula[0:10]


trimmed_cedulas = run_over_list(
    cc_without_duplicates, trim_cedula_length, list_name)


def get_error_cedulas(cedula):
    cedulaLength = len(cedula)
    if(cedulaLength > 10 or cedulaLength < 7):
        return cedula


def get_empty_cedulas(cedula):
    cedulaLength = len(cedula)
    if(cedulaLength == 0):
        return cedula


def get_possible_cedulas(cedula):
    cedulaLength = len(cedula)
    if(cedulaLength > 6 and cedulaLength < 11):
        return cedula


error_cedulas = run_over_list(trimmed_cedulas, get_error_cedulas, list_name)
empty_cedulas = run_over_list(trimmed_cedulas, get_empty_cedulas, list_name)
possible_cedulas = run_over_list(
    trimmed_cedulas, get_possible_cedulas, list_name)

df_error_cedulas_ungrouped = dataframe_from_dict(error_cedulas, list_name)
df_empty_cedulas_ungrouped = dataframe_from_dict(empty_cedulas, list_name)
df_possible_cedulas_ungrouped = dataframe_from_dict(
    possible_cedulas, list_name)


print("df_error_cedulas_ungrouped: ")
print(df_error_cedulas_ungrouped, "\n")

print("df_empty_cedulas_ungrouped: ")
print(df_empty_cedulas_ungrouped, "\n")

print("df_possible_cedulas_ungrouped: ")
print(df_possible_cedulas_ungrouped, "\n")
