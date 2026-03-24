# Quicksort Algorithmn

# This implementation of quicksort is not in-place, meaning it does not modify the original list. Instead, it creates new lists for the less than, equal to, and greater than elements relative to the pivot. The original list remains unchanged throughout the sorting process.
def quick_sort(integers):
    if len(integers) <= 1:
        return integers

    pivot = integers[0]
    less = []
    equal = []
    greater = []

    for x in integers[1:]:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)

    return quick_sort(less) + [pivot] + equal + quick_sort(greater)


# Test cases
print(quick_sort([]))                                      # []
original = [20, 3, 14, 1, 5]
quick_sort(original)
print(original)                                            # [20, 3, 14, 1, 5] (unchanged)
print(quick_sort([20, 3, 14, 1, 5]))                       # [1, 3, 5, 14, 20]
print(quick_sort([83, 4, 24, 2]))                          # [2, 4, 24, 83]
print(quick_sort([4, 42, 16, 23, 15, 8]))                  # [4, 8, 15, 16, 23, 42]
print(quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56])) # [11, 11, 18, 18, 23, 23, 56, 56, 87, 87]