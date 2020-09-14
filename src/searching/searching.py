# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # setting base case if target is not found
    if start > end:
        return -1

    # setting the middle index of given data
    mid_idx = (start + end) // 2
    if arr[mid_idx] == target:
        return mid_idx
    elif arr[mid_idx] < target:
        return binary_search(arr,target,mid_idx + 1,end)
    else:
        return binary_search(arr, target, start, mid_idx - 1)



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here