# Binary Search Algorithm

# This algorithm works on sorted lists. It repeatedly divides the search interval in half until the target value is found or the search interval is empty.
def binary_search(search_list, value): # search_list must be sorted
    path_to_target = [] # This list will keep track of the values we check during the search process
    low = 0
    high = len(search_list) - 1
    while low <= high: # While there are still elements to check
        mid = (low + high) // 2
        value_at_middle = search_list[mid]
        path_to_target.append(value_at_middle) # Add the value at the middle index to the path list

        if value == value_at_middle: # If the value at the middle index is the target value, we have found it
            return path_to_target, f'Value found at index {mid}'
        elif value > value_at_middle: # If the target value is greater than the value at the middle index, we need to search in the right half of the list
            low = mid + 1
        else: # If the target value is less than the value at the middle index, we need to search in the left half of the list
            high = mid - 1

    return [], "Value not found"

print(binary_search([1, 2, 3, 4, 5], 3))
print(binary_search([1, 2, 3, 4, 5, 9], 4))
print(binary_search([1, 3, 5, 9, 14, 22], 10))

## Output:
# ([3], 'Value found at index 2')
# ([3, 4], 'Value found at index 3')
# ([], 'Value not found')