def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr



test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]

print(bubble_sort(test))
