# https://www.youtube.com/watch?v=0SkOjNaO1XY&t=316s
def quicksort(arr, l, r): # l and r represent indices of the section that we want to sort (left and right)
    if l >= r:
        return
    p = partition(arr, l, r) 
    # partition will return new location of the pivot
    # goal of parition is to separate array into 2 groups 
    #(group that is less than the pivot and group that is greater than the pivot)

    # now we need to sort the two subarrays that are left and right of the pivot 

    quicksort(arr, l, p - 1) # EX: [-2, -1, 0, 1, 2, 4, 3] l:p - 1 = [-2, -1, 0]
    quicksort(arr, p + 1, r) # EX: [-2, -1, 0, 1, 2, 4, 3] p + 1:r = [2, 4, 3]

    return arr

def partition(arr, l, r):
    # we will use i and j as indexes and a pointer to the pivot
    # j = current number examined
    # all numbers before i should be less than the pivot and all numbers between i and j should be greater
    # if not, then increment i or j and swap numbers

    # after partitioning, swap pivot with i + 1 

    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] < pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    temp = arr[i + 1]
    arr[i + 1] = arr[r]
    arr[r] = temp
    return i + 1

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test, 0, len(test) - 1))
