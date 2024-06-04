def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

array_desc = [10, 8, 6, 4, 2, 0]
sorted_array = selection_sort(array_desc)
print(sorted_array)
