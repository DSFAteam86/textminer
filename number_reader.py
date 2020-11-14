import os
import re
from miner import TextMiner


def run_over_list(data, callback, list_name):

    output_list = []
    for object_element in data:
        temp_list = []
        for element in object_element[list_name]:
            result = callback(element)
            if(result != None):
                temp_list.append(result)

        if(len(temp_list) > 0):
            output_list.append({
                "uid": object_element["uid"],
                list_name: temp_list
            })

    return output_list


def find_numbers_with(path, search_terms, value_name, left_offset=0, right_offset=40):
    data = []

    for root, directories, files in os.walk(path, topdown=False):
        contract_list = []
        for name in files:
            contract_file = open(os.path.join(root, name), 'r')
            contract_content = contract_file.read()
            contract_list.append(contract_content)

            mine = TextMiner(contract_list)
            contract_list = []

            data.append({
                "uid": name,
                value_name: mine.get_chunks_in_array(search_terms,
                                                     left=left_offset,
                                                     right=right_offset
                                                     )
            })

    return data


def get_consecutives(inputString):
    string = re.sub('[^\w\s]', '', inputString)
    stringLength = len(string)

    consecutiveNumbers = ""
    counter = 0

    while(counter < stringLength):
        currentElement = string[counter]
        isCounterInRange = counter < stringLength - 1

        foundConsecutiveNumbers = len(consecutiveNumbers) > 0
        nextElement = string[counter + 1] if isCounterInRange else None

        if(isCounterInRange):
            isNextOfTypeNumber = nextElement.isnumeric()

        if(currentElement.isnumeric() and isNextOfTypeNumber):
            consecutiveNumbers += currentElement

        elif(currentElement.isnumeric() and not isNextOfTypeNumber and not foundConsecutiveNumbers):
            break

        counter += 1

    return consecutiveNumbers


def remove_array_duplicates(array):
    return list(dict.fromkeys(array))


def remove_duplicates(object_list, list_name):

    list_without_duplicates = []

    for object_element in object_list:

        list_without_duplicates.append({
            "uid": object_element["uid"],
            list_name: remove_array_duplicates(object_element[list_name])
        })

    return list_without_duplicates


def trim_data(data, list_name, start=0, end=0):
    trimmed_data = []
    for object_element in data:
        temp_data = []
        for element in object_element[list_name]:
            temp_data.append(element[start: end])

        trimmed_data.append({
            "uid": object_element["uid"],
            list_name: temp_data
        })

    return trimmed_data
