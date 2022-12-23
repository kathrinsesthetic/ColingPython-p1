import collections


def my_sort(s):
    m = {}
    for element in s:
        if element in m:
            m[element] += 1
        else:
            m[element] = 1
    result = ""
    for element, count in m.items():
        result += element * count
    return result


print(my_sort("dfgdfgdfgdfefsdfs"))
