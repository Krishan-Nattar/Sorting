# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    array_1_index = 0
    array_2_index = 0
    merged_array_iterator = 0

    while array_1_index < len(arrA) and array_2_index < len(arrB):
        if arrA[array_1_index] < arrB[array_2_index]:
            merged_arr[merged_array_iterator] = arrA[array_1_index]
            merged_array_iterator += 1
            array_1_index += 1
        else:
            merged_arr[merged_array_iterator] = arrB[array_2_index]
            merged_array_iterator += 1
            array_2_index += 1
    while array_1_index < len(arrA):
        merged_arr[merged_array_iterator] = arrA[array_1_index]
        merged_array_iterator += 1
        array_1_index += 1
    while array_2_index < len(arrB):
        merged_arr[merged_array_iterator] = arrB[array_2_index]
        merged_array_iterator += 1
        array_2_index += 1

    return merged_arr


# arr1 = [2,4,6,8,10,12,14,16]
arr2 = [1,3,7,4,5]

# print(merge(arr1, arr2))

# Am I supposed to use the helper array in the merge_sort function?! Because I can't figure that out

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # print("Top:\n" + str(arr))
    if len(arr)>1:
        # print("Second\n" + str(arr))

        middle = int(len(arr)/2)

        array_left = arr[:middle]
        array_right = arr[middle:]

        merge_sort(array_left)
        merge_sort(array_right)

        array_1_index = 0
        array_2_index = 0
        merged_array_iterator = 0

        while array_1_index < len(array_left) and array_2_index < len(array_right):
            if array_left[array_1_index] < array_right[array_2_index]:
                arr[merged_array_iterator] = array_left[array_1_index]
                merged_array_iterator += 1
                array_1_index += 1
            else:
                arr[merged_array_iterator] = array_right[array_2_index]
                merged_array_iterator += 1
                array_2_index += 1
        while array_1_index < len(array_left):
            arr[merged_array_iterator] = array_left[array_1_index]
            merged_array_iterator += 1
            array_1_index += 1
        while array_2_index < len(array_right):
            arr[merged_array_iterator] = array_right[array_2_index]
            merged_array_iterator += 1
            array_2_index += 1


    return arr
arr3 = [10,9,8,7,1,2,5,6,7,4,2,0]
merge_sort(arr3)
print("Final array: " +str(arr3))



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

