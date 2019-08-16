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
# print(bubble_sort(num_array))

num_array2 = [1,4,1,2,7,5,2]
# STRETCH: implement the Count Sort function below



# [[0, 0], [1, 2], [2, 2], [3, 0], [4, 1], [5, 1], [6, 0], [7, 1]]


def count_sort(arr, maximum=-1):
    maximum = max(arr)
    count_array = []
    return_arr = []
    # print(maximum)
    for i in range(0, maximum +1):
        count = arr.count(i)
        count_array.append([i, count])
    for i in count_array:
        while i[1] > 0:
            return_arr.append(i[0])
            i[1] -= 1

    # print(count_array)
    # print(return_arr)

    return arr

# count_sort(num_array)