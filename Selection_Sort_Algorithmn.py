# Selection Sort Algorithm

# This algorithm divides the input list into two parts: the sorted part and the unsorted part. It repeatedly selects the smallest (or largest) element from the unsorted part and moves it to the end of the sorted part.
def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        if min_index != i:
            lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

print(selection_sort([33, 1, 89, 2, 67, 245]))
print(selection_sort([5, 16, 99, 12, 567, 23, 15, 72, 3]))
print(selection_sort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]))


## Output:
# [1, 2, 33, 67, 89, 245]
# [3, 5, 12, 15, 16, 23, 72, 99, 567]
# [1, 1, 2, 2, 4, 8, 23, 32, 43, 43, 55, 63, 92, 123, 123, 234, 345, 5643]