# TO-DO: Complete the selection_sort() function below 

num_array = [2,5,324,3,1,224,54,98,4,24]

def selection_sort( arr ):
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

print(selection_sort(num_array))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr