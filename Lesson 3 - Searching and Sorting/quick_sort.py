"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    quick_sort_sub_arrays(array, 0, len(array) - 1)
    return array
    
def quick_sort_sub_arrays(array, start, end):
    if start >= end:
        return
    pivot_pos = (start + end) // 2
    pivot_value = array[pivot_pos]
    swap(pivot_pos, end, array)
    i = start - 1
    j = end
    while i < j:
        i += 1
        while i < end and array[i] < pivot_value:
            i += 1
        j -= 1
        while j >= 0 and array[j] > pivot_value:
            j -= 1
        if i < j:
            swap(i, j, array)
    swap(i, end, array)
    quick_sort_sub_arrays(array, start, i - 1)
    quick_sort_sub_arrays(array, i + 1, end)
    
    
def swap(pos1, pos2, array):
    temp = array[pos1]
    array[pos1] = array[pos2]
    array[pos2] = temp

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
