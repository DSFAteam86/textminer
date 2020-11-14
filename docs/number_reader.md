# number_reader

This file will serve as documentation for [number_reader.py](../number_reader.py)

### run_over_list(data, callback, list_name)

Iterates over a list of dictionaries and, once it's in one of the dictionaries, searches for a key that has an array as value

Params:

- **data**: List of objects or dictionaries
- **list_name**: name of the array in a dictionary
- **callback(array_element)**: function to perform actions to the items in the array

### run_over_list(data, callback, list_name)

Iterates over a list of dictionaries and, once it's in one of the dictionaries, searches for a key that has an array as value

Params:

- **data**: List of objects or dictionaries
- **list_name**: name of the array in a dictionary
- **callback(array_element)**: function to perform actions to the items in the array

### find_numbers_with(path, search_terms, value_name, left_offset=0, right_offset=40)

Does the initial search in the .txt files but without filtering any of its information

- **path**: The path of the files in [config.py](../config.py)
- **search_terms**: Array of words to be searched
- **value_name**: Name of the array that will contain the search_terms (usually a plural version of the search term)

* **left_offset:** how many characters should appear before the word
* **right_offset**: how many characters should appear after the word

left_offset and right_offset are similar to the get_chunk functions in [Miner](miner.md)

### get_consecutives(inputString)

Takes the first ocurrence of a sequence of numbers in a string. Example

    consecutives = get_consecutives("it will read this number: 123456789 but not this one: 66")
    print(consecutives)

    // output:
    // 123456789

it finds exactly the first sequence of numbers not separated by spaces. Example:

    consecutives = get_consecutives("acbd 12345 7 9 76 fghi")
    print(consecutives)

    // output
    // 12345

### remove_duplicates(object_list, list_name)

Removes duplicates in an array contained in a list of objects. Example

    list = [
      {"a": "some value", "bs": ["Hello", "Hello", "world"]},
      {"a": "some value", "bs": ["Hola", "Hola", "mundo"]}
    ]
    no_duplicates = remove_duplicates(list, "bs")

    print(no_duplicates)

    // output:

    [
      {"a": "some value", "bs": ["Hello", "world"]},
      {"a": "some value", "bs": ["Hola", "mundo"]}
    ]

- **object_list:** List of objects
- **list_name:** key name of list

### trim_data(data, list_name, start=0, end=0)

cuts the values off the left and right of a string in an array contained in a list of dictionaries

- **object_list:** List of dictionaries
- **list_name:** key name of list
- **start:** number of values to be removed from the start of the string
- **end:** number of values to be removed from the end of the string
