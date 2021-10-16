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


# This function recursively calls itself until it either finds the
# requested key, or finishes searching.
# Note to self: this runs in O(log N) time.
def binarySearchRecursive(input_list, key, low, high):
    if low > high:
        return False
    else:
        mid = findMidPoint(low, high)
        print(mid)
        if input_list[mid] == key:
            return True
        elif input_list[mid] > key:
            high = mid - 1
            # The teacher suggests passing mid - 1 as a parameter, but I'm uncomfortable
            # making the change in the call.
            return binarySearchRecursive(input_list, key, low, high)
        else:
            low = mid + 1
            return binarySearchRecursive(input_list, key, low, high)


a_list = [1, 2, 4, 5, 20]
a_key = 5
a_low = 0
a_high = 4

print(binarySearchIterative(a_list, a_key))
print(binarySearchRecursive(a_list, a_key, a_low, a_high))