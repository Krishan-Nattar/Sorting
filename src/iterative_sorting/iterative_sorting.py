# TO-DO: Complete the selection_sort() function below

num_array = [2, 5, 324, 3, 1, 224, 54, 98, 4, 24]


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):

        cur_index = i
        smallest_index = cur_index

        for x in range(i+1, len(arr)):
            if arr[smallest_index] > arr[x]:
                smallest_index = x
        hold_first = arr[cur_index]
        hold_second = arr[smallest_index]

        arr[cur_index] = hold_second
        arr[smallest_index] = hold_first

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # TO-DO: swap

    return arr


# print(selection_sort(num_array))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # index = 0
    loop = True
    count = 0

    while loop:
        count = 0
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                hold_value = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = hold_value
                count += 1
        if count == 0:
            loop = False

    # select item

    # check current value vs the next item

    # if second item is smaller, switch the values

    # move onto the next item

    # repeat

    return arr
# print(num_array)
print(bubble_sort(num_array))

# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
