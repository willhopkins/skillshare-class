# Implements a binary search algorithm.

# Helper function to find mid-point.
def findMidPoint(low, high):
    # Use int() function to coerce to integer
    mid = (low + high) // 2
    return mid


# Iterative implementation
# For this function, assume the input is a list type, and sorted.
def binarySearchIterative(input_list, key):
    low = 0
    # Reminder to self, len will be the number of indices + 1
    high = len(input_list) - 1

    while low <= high:
        mid = (low + high) // 2
        print(mid)
        if input_list[mid] == key:
            return True
        elif input_list[mid] > key:
            high = mid - 1
        else:
            low = mid + 1

    return False


a_list = [1, 2, 4, 5, 20]
a_key = 5

print(binarySearchIterative(a_list, a_key))