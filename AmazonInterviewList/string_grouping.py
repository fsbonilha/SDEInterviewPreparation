# Given an array of strings, group the strings that are composed by the same 
# characters, returning an array of arrays.

# For example, given:
# ["124", "412", "425", "241", "524", "324", "2141"]

# Return:
# [
#     ["241", "124","412"],
#     ["524","425"],
#     ["324"],
#     ["2141"]
# ]

from typing import List

def group_strings(strings: List[str]) -> List[List[str]]:
    result = dict()

    for string in strings:
        char_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for number in string:
            char_counts[int(number)] += 1
        result[tuple(char_counts)] = result.get(tuple(char_counts), []) + [string]
    return result.values()

a = ["124", "412", "425", "241", "524", "324", "2141"]

print(group_strings(a))