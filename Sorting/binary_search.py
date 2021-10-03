#  Binary Search Algorithm

import math

def binary_search(value, list_to_search):
    
    search_value = -1
    max_index = len(list_to_search) - 1
    min_index = 0
    middle_index = int(math.floor( (max_index + min_index) / 2))
    current_element = list_to_search[middle_index]

    while max_index >= min_index:

        if current_element == value:
            return current_element

        elif value > current_element:
            min_index = middle_index + 1

        elif value < current_element:
            max_index = middle_index - 1
            
        middle_index = int(math.floor( (min_index + max_index) / 2))
        current_element = list_to_search[middle_index]

    return search_value


id_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
short_list = ['allie', 'ben', 'charlie', 'danielle', 'emilio', 'fred', 'gina', 'henry', 'isabella']
print(binary_search('gina', short_list))