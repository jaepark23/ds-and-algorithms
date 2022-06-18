# https://www.youtube.com/watch?v=cVZMah9kEjI

def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr) // 2]
        right_arr = arr[len(arr) // 2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i, j, k = 0, 0, 0 # left, right, and merged array index

        # merge the two sorted arrays together
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        # given that the while loop above ends without the array completing, that means that one whole array is remaining, since left and right arrays were already sorted,
        # we can just add the leftover array to the end of the final array 
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
merge_sort(test)
print(test)
