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

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    while True:
        swapped = False
        # iteration = 0
        for i in range(0, len(arr)-1 - i):
            if arr[i] > arr[i+1]:
                hold_value = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = hold_value
                swapped = True
                # iteration += 1
        if swapped == False:
            break

    return arr

num_array2 = [1,4,1,2,7,5,2]
# STRETCH: implement the Count Sort function below

# loop through, check for instance, increment

def count_sort(arr, maximum=-1):
    maximum = max(arr) # loop 1
    count_array = []
    return_arr = []
    for i in range(0, maximum +1): # loop 2
        count = arr.count(i)
        count_array.append([i, count])
    # print(count_array)
    for i in count_array: # loop 3
        while i[1] > 0:
            return_arr.append(i[0])
            i[1] -= 1
    return return_arr

# Alternative using a dictionary
def count_sort2(arr, maximum=-1):

    count_dict = {}
    return_arr = []
    lowest = arr[0]
    highest = arr[0]

    for i in arr:
        if i < lowest:
            lowest = i
        if i > highest:
            highest = i
        if str(i) in count_dict.keys(): 
            count_dict[str(i)] += 1
        else:
            count_dict[str(i)] = 1
            
    for i in range(lowest, highest+1):
        while str(i) in count_dict.keys(): 
            count_dict[str(i)] -= 1
            return_arr.append(i)
            if count_dict[str(i)] == 0:
                break
    return return_arr

print(count_sort2(num_array))