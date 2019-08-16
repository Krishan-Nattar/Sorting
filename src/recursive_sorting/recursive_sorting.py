# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    array_1_index = 0
    array_2_index = 0
    merged_array_iterator = 0

    while merged_array_iterator < elements:
        if array_1_index < len(arrA) and array_2_index < len(arrB):
            if arrA[array_1_index] < arrB[array_2_index]:
                merged_arr[merged_array_iterator] = arrA[array_1_index]
                merged_array_iterator += 1
                array_1_index += 1
            else:
                merged_arr[merged_array_iterator] = arrB[array_2_index]
                merged_array_iterator += 1
                array_2_index += 1
        elif array_1_index < len(arrA):
            merged_arr[merged_array_iterator] = arrA[array_1_index]
            merged_array_iterator += 1
            array_1_index += 1
        else:
            merged_arr[merged_array_iterator] = arrB[array_2_index]
            merged_array_iterator += 1
            array_2_index += 1

    return merged_arr


arr1 = [1, 3, 5, 7, 9, 11, 14, 16, 111, 245, 667]
arr2 = [2, 4, 9, 10, 22, 44, 55, 66, 77, 88, 99, 204, 302]

print(merge(arr1, arr2))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    # if array is more than one, split it in half

    # left array = something
    # right array = something else

    # sort the first half
    # sort the second half   THESE TWO ARE RECURSIVE... The are essentially called back into the merge_sort function

    # if the length of the data sent back is less than 2, don't run the recursion

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
