# 🧮 Python Algorithms Collection

A collection of classic computer science algorithms implemented in Python — covering **search**, **sort**, **numerical methods**, and **validation techniques**.

---

## 📁 Files Overview

| File | Algorithm | Category |
|------|-----------|----------|
| `Binary_Search_Algorithmn.py` | Binary Search | Search |
| `Bisection_Method.py` | Bisection Method | Numerical Methods |
| `Luhn_Algorithmn.py` | Luhn Algorithm | Validation |
| `Merge_Sort_Algorithmn.py` | Merge Sort | Sorting |
| `Quicksort_Algorithmn.py` | Quicksort | Sorting |
| `Selection_Sort_Algorithmn.py` | Selection Sort | Sorting |

---

## 🔍 Binary Search — `Binary_Search_Algorithmn.py`

**Category:** Search Algorithm  
**Time Complexity:** O(log n) | **Space Complexity:** O(1)

### How It Works

Binary Search operates on **sorted lists** by repeatedly halving the search interval:

1. Set `low = 0` and `high = len(list) - 1`.
2. Compute the midpoint `mid = (low + high) // 2`.
3. Compare the target value against `list[mid]`:
   - **Equal** → target found; return the index.
   - **Greater** → search the right half (`low = mid + 1`).
   - **Less** → search the left half (`high = mid - 1`).
4. Repeat until the target is found or the interval is empty.

The function also tracks the **path of values checked**, returning it alongside the result message.

### Example

```python
binary_search([1, 2, 3, 4, 5], 3)
# → ([3], 'Value found at index 2')

binary_search([1, 3, 5, 9, 14, 22], 10)
# → ([], 'Value not found')
```

> ⚠️ **Prerequisite:** The input list must be sorted before calling this function.

---

## √ Bisection Method — `Bisection_Method.py`

**Category:** Numerical Methods  
**Convergence:** Guaranteed for continuous functions with sign changes

### How It Works

The Bisection Method finds the **square root** of a number by narrowing an interval `[low, high]` until the midpoint is within the desired tolerance:

1. Handle edge cases: negative numbers raise a `ValueError`; `0` and `1` return immediately.
2. Set `low = 0` and `high = max(1, target)`.
3. Compute `mid = (low + high) / 2` and check `mid²` against the target:
   - If `|high - low| ≤ tolerance` → converged; return `mid` as the root.
   - If `mid² < target` → move `low = mid`.
   - Otherwise → move `high = mid`.
4. Repeat for up to `max_iterations` steps.

Accepts configurable `tolerance` (default `1e-7`) and `max_iterations` (default `100`).

### Example

```python
square_root_bisection(81, 1e-3, 50)
# → The square root of 81 is approximately 9.000000000000002

square_root_bisection(225, 1e-7, 10)
# → Failed to converge within 10 iterations
```

---

## 💳 Luhn Algorithm — `Luhn_Algorithmn.py`

**Category:** Checksum / Validation  
**Use Case:** Credit card number validation

### How It Works

The Luhn Algorithm validates identification numbers (e.g., credit card numbers) via a checksum:

1. Strip all dashes (`-`) and spaces from the input.
2. Convert each character to an integer.
3. Starting from the **second-to-last digit** going right to left, double every second digit.
4. If any doubled value exceeds `9`, subtract `9` from it.
5. Sum all digits. If `total % 10 == 0` → **VALID!**, otherwise → **INVALID!**

### Example

```python
verify_card_number('4111-1111-1111-1111')   # → 'VALID!'
verify_card_number('1234 5678 9012 3456')   # → 'INVALID!'
```

---

## 🔀 Merge Sort — `Merge_Sort_Algorithmn.py`

**Category:** Sorting Algorithm (Divide & Conquer)  
**Time Complexity:** O(n log n) | **Space Complexity:** O(n)

### How It Works

Merge Sort recursively splits and merges arrays **in-place**:

1. **Divide:** Split the array at the midpoint into `left_part` and `right_part`.
2. **Recurse:** Call `merge_sort` on each half.
3. **Merge:** Compare elements from both halves one by one, writing the smaller value back into the original array at `sorted_index`.
4. Append any remaining elements from either half.

> The function modifies the original list **in-place** and returns `None`.

### Example

```python
numbers = [4, 10, 6, 14, 2, 1, 8, 5]
merge_sort(numbers)
print(numbers)
# → [1, 2, 4, 5, 6, 8, 10, 14]
```

---

## ⚡ Quicksort — `Quicksort_Algorithmn.py`

**Category:** Sorting Algorithm (Divide & Conquer)  
**Time Complexity:** O(n log n) average, O(n²) worst | **Space Complexity:** O(n)

### How It Works

This is a **non-in-place** implementation of Quicksort — it creates new lists rather than modifying the original:

1. **Base case:** Return the list immediately if it has 0 or 1 elements.
2. **Pivot:** Select the first element as the pivot.
3. **Partition:** Iterate over the remaining elements, distributing them into `less`, `equal`, or `greater` buckets.
4. **Recurse & Combine:** Return `quick_sort(less) + [pivot] + equal + quick_sort(greater)`.

> The **original list is never modified**. A new sorted list is returned.

### Example

```python
print(quick_sort([20, 3, 14, 1, 5]))
# → [1, 3, 5, 14, 20]

original = [20, 3, 14, 1, 5]
quick_sort(original)
print(original)
# → [20, 3, 14, 1, 5]  ← unchanged
```

---

## 🔃 Selection Sort — `Selection_Sort_Algorithmn.py`

**Category:** Sorting Algorithm  
**Time Complexity:** O(n²) | **Space Complexity:** O(1)

### How It Works

Selection Sort divides the list into a **sorted** and **unsorted** region, growing the sorted region one element at a time:

1. For each position `i`, scan the unsorted portion (`i+1` to end) to find the index of the minimum element.
2. If the minimum is not already at position `i`, swap it there.
3. Advance `i` and repeat until the entire list is sorted.

> Modifies and returns the list **in-place**.

### Example

```python
print(selection_sort([33, 1, 89, 2, 67, 245]))
# → [1, 2, 33, 67, 89, 245]

print(selection_sort([5, 16, 99, 12, 567, 23, 15, 72, 3]))
# → [3, 5, 12, 15, 16, 23, 72, 99, 567]
```

---

## 🚀 Running the Scripts

Each script can be run directly with Python 3:

```bash
python Binary_Search_Algorithmn.py
python Bisection_Method.py
python Luhn_Algorithmn.py
python Merge_Sort_Algorithmn.py
python Quicksort_Algorithmn.py
python Selection_Sort_Algorithmn.py
```

No external dependencies are required — the standard Python 3 library is sufficient for all scripts.

---

## 📊 Algorithm Comparison

| Algorithm | Type | Time Complexity | Space Complexity | In-Place? |
|-----------|------|-----------------|------------------|-----------|
| Binary Search | Search | O(log n) | O(1) | ✅ |
| Bisection Method | Numerical | O(log(1/ε)) | O(1) | N/A |
| Luhn Algorithm | Validation | O(n) | O(n) | ✅ |
| Merge Sort | Sort | O(n log n) | O(n) | ✅ |
| Quicksort | Sort | O(n log n) avg | O(n) | ❌ |
| Selection Sort | Sort | O(n²) | O(1) | ✅ |
