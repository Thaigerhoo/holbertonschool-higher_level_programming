#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_elements = set()

    for element in my_list:
        unique_elements.add(element)

    return sum(unique_elements)
