# Perform a linear search algorithm in Python.

def linearSearch(input_object, key):
    position = 0
    flag = False
    while position < len(input_object) and not flag:
        if input_object[position] == key:
            flag = True
        else:
            position += 1
    return flag

input_object = [1, 2, 3, 4, 5]
key = 3
# key = 8

print(linearSearch(input_object, key))
