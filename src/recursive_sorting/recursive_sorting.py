# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    i = 0
    while len(arrA) > 0 or len(arrB) > 0:
        # print(i)
        if len(arrA) == 0:
            merged_arr[i] = arrB.pop(0)
        elif len(arrB) == 0:
            merged_arr[i] = arrA.pop(0)

        # two statements above are for edge cases when arrA and arrB are empty
        elif arrA[0] <= arrB[0]:
            merged_arr[i] = arrA.pop(0)
        else:
            merged_arr[i] = arrB.pop(0)
        i += 1    
    return merged_arr

# FAILED / OVERLY COMPLEX DOUBLE CURSOR METHOD:

# def merge( arrA, arrB ):
#     elements = len( arrA ) + len( arrB )
#     merged_arr = [0] * elements
#     # TO-DO
#     i = 0
#     a_cursor = 0
#     b_cursor = 0
#     while i < len(merged_arr):
#         if arrA[a_cursor] <= arrB[b_cursor]:
#             merged_arr[i] = arrA[a_cursor]
#             a_cursor += 1
#         else:
#             merged_arr[i] = arrA[b_cursor]
#             b_cursor += 1
#         i += 1    

# MY TESTS:
test_1 = [2, 4, 5, 9]
test_2 = [2, 3, 3, 9, 10]
# print(merge(test_1, test_2))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # BASE CASE: element is sorted -- how do you know? only one item in arr
    if len(arr) < 2: # use < 2 to account for edge case of empty list
        return arr
    # if arr contains more than two elements, split and sort
    i = len(arr) // 2
    arrA = merge_sort(arr[:i])
    arrB = merge_sort(arr[i:])
    arr = merge(arrA, arrB)

    return arr

# MY TESTS:
test_3 = [10,6,1,7,8,4,3,1,4,5,6,8]
test_4 = []
test_5 = [5]
print(merge_sort(test_3))
print(merge_sort(test_4))
print(merge_sort(test_5))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
