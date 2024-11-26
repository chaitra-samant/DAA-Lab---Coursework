
def is_sorted(arr)->bool:
    """
    This function checks if the given list for binary search is sorted in ascending order 

    Arguments:
        arr (list):The list which needs to be checked if it's sorted

    Returns:
        bool: True if list is sorted. False if it isn't

    """
    for i in range(1,len(arr)):
        if(arr[i]<arr[i-1]):
            return False
    
    return True



def display_output(x):
    """
    This function displays output after searching

    Arguments:
        x (int): The index returned after calling respective search function

    Returns:
        void: no value returned

    """
    if x>-1:
        print(f"Value {target} found at position {x}")
    else:
        print(f"Value {target} is not found in the given list")
    



def linear_search(arr, target) -> int:
    """
    This function performs linear search on an list of elements

    Arguments:
        arr (list): The list in which target value needs to be searched
        target (int): This is the value that we need to search

    Returns:
        int: The index of the target if it is found and -1 if it isn't 
    
    """
    if arr:
        ind = -1
        for i in range(len(arr)):
            if arr[i] == target:
                ind = i
                break 
        return ind
    else:
        print("List is empty")
        exit(1)



def binary_search(arr, target, beg, end) -> int:
    """
    This function performs binary search on a sorted list of elements

    Arguments:
        arr (list): The sorted list in which target value needs to be searched
        target (int): This is the value that we need to search

    Returns:
        int: The index of the target if it is found and -1 if it isn't 
    
    """
    if arr:
        if beg <= end:
            mid = (beg + end) // 2   
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                return binary_search(arr, target, beg, mid - 1)
            else: 
                return binary_search(arr, target, mid + 1, end)
        else:
            return -1
    else:
        print("List is empty")
        exit(1)




# Initialising list and variables
arr = [6,3,1,9,13]
target = 9
beg, end = 0, len(arr) - 1

# Displaying Input
print("List:",arr)
print("Target:",target)


# Linear Search
x = linear_search(arr, target)
display_output(x)

# Binary Search
if(is_sorted(arr)):
    x = binary_search(arr, target, beg, end)
    display_output(x)
else:
    print("List isn't sorted, Binary Search can only be performed on sorted lists")
