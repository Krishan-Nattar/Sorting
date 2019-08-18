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

arr2 = [1,3,7,4,5]


# Am I supposed to use the helper array in the merge_sort function?! Because I can't figure that out

#Merge Sort Function
def merge_sort(arr):
    if len(arr)>1: 

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

arr3 = [4,3,2,1]
merge_sort(arr3)
print("Final array: " +str(arr3)) 



# STRETCH: implement an in-place merge sort algorithm

def merge_sort_in_place(arr):
    grouping = 1  
    while grouping <= len(arr):  

        for left_iterator in range(0, len(arr), grouping * 2): 
            right_boundary = min(len(arr), left_iterator + 2 * grouping) 
            middle_iterator = left_iterator + grouping
            
            while left_iterator < middle_iterator and middle_iterator < right_boundary:

                if arr[left_iterator] < arr[middle_iterator]: 
                    left_iterator += 1 
                else: 
                    move_to_left_iterator_index = arr[middle_iterator] 
                    arr[left_iterator + 1: middle_iterator + 1] = arr[left_iterator:middle_iterator] 
                    arr[left_iterator] = move_to_left_iterator_index 
                    left_iterator +=1 
                    middle_iterator +=1
        grouping *= 2
    return arr

print(merge_sort_in_place([8,3,7,2]))


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


# def merge_sort_in_place(arr, l, r):
#     # TO-DO

#     return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr

