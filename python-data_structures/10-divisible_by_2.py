#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mul_two = []
    for num in my_list:
        if num % 2 == 0:
            mul_two.append(True)
        else:
            mul_two.append(False)
            return mul_two
