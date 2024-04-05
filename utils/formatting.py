
from collections import defaultdict

def combine_dicts(dicts: list[dict]):
    combined_dict = defaultdict(list)
    for d in dicts:
        for key, value in d.items():
            combined_dict[key].append(value)
    return dict(combined_dict)

def print_dict(dict: dict):
    for key in dict.keys():
        print(f"{key} : {dict[key]}")

def dict_to_stringlist(dict: dict) -> list[str]:
    list_of_strings: list[str] = []
    for key in dict.keys():
        list_of_strings.append(f"{key} : {dict[key]}")
    
    return list_of_strings
