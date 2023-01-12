#  John Daggs

#  11/12/2021

#  Purpose of Lab06.py:
# The purpose of Lab06.py is to encompass searching, recursion, and hashing. This file should include a binary search
# function, sequential search function, smart sequential search function, a max function that uses recursion, and a
# hashing function. Then, each function is utilized in main.

#  collaborators/resources -
#  Class Notes/Powerpoint/Code Examples/Textbook on Searching, Recursion, Hashing

def binary_search(some_list, some_target): # returns true or false depending on if the target is found
    first = 0
    last = len(some_list) - 1
    found = False
    while first <= last and not found:  # loop while first is greater than last and found = False
        mid = (first + last) // 2  # init. mid variable
        if some_list[mid] == some_target:  # if mid is the target
            found = True  # found is true
        else:   # mid is not target
            if some_target < some_list[mid]:  # target is less than mid
                last = mid - 1  # last is set to mid - 1, index before mid
            else:  # target is greater than mid
                first = mid + 1  # last is set to mid + 1, index after mid
    return found  # returning found to show true, false depending on whether value is found


def sequential_search(some_list,some_target): # returns true or false for whether the target is found and
    # the location of the target
    pos = 0  # initializing position value
    found = False  # initializing found value

    while pos < len(some_list) and not found:  # loop like position variable is less than the length and found = False
        if some_list[pos] == some_target:  # if value of list at position equal target
            found = True  # target found, found = True
        else:   # value of list at position is not target
            pos = pos + 1  # add one to position, next index in list

    return found, pos  # returning position value, and whether it was found or not


def smart_sequential_search(some_list, some_target):  # returns true or false for whether the target is found and
    # the location of the target, list must be sorted to work properly
    pos = 0  # initialize position
    found = False  # initialize found variable at False
    while pos < len(some_list) and not found:  # loop like position variable is less than the length and found = False
        if some_list[pos] == some_target: # if value of list at position equal target
            found = True # target found, found = True
        else:  # value of list at position is not target
            if some_list[pos] > some_target:  # if the value is greater than the target
                found = False  # found is false, target can not be found
            else:  # value is less than the target
                pos = pos + 1  # position is moved u[
                found = False  # found is false, loop continues
    return found, pos  # returning position value and found value


def max(list):  # function, takes in a list parameter and returns max
    if len(list) == 1:  # if the length is one
        return list[0]  # the max is at index zero, return index zero
    else:               # length greater than one
        m = max(list[1:])  # m variable set to the max of the list from index one through the end, RECURSIVE CALL
        return m if m > list[0] else list[0]  # RETURN max value if its greater than index zero value, else return
        # index zero as max


def hash(item_list, table_size):
    hash_table = dict([(i, None) for i, x in enumerate(range(table_size))])  # initializing a hash table for the values
    # creating indices in the hash table based on the size of the list parameter
    for item in item_list:  # iterate through list
        i = item % table_size  # creating hash value
        print("The hash for %s is %s" % (item, i))  # printing out hash value
        hash_table[i] = item  # adding hash value to hash table

    return hash_table  #returning hash table


def main():
    print(binary_search([1, 2, 3, 5, 8], 6))  # False
    print(binary_search([1, 2, 3, 5, 8], 5))  # True
    print(sequential_search([11, 23, 58, 31, 56, 77, 43, 12, 65, 19], 31))  # (True, 3)
    print(max([11, 23, 58, 31, 56, 77, 43, 12, 65, 19]))  # 77
    print(smart_sequential_search([1, 4, 5, 23, 31, 56, 57, 71, 105], 31))  # (True, 4)
    item_list = [1111111111, 2222222222, 3333333333, 4444444444, 5555555555, 6666666666, 7777777777, 8888888888, 9999999999]
    print(hash(item_list, len(item_list)))

main()