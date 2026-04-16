# 📘 Binary Search Variations

## 📍 Overview
Binary Search is not just one algorithm. It has multiple variations depending on the problem type.

Time Complexity: O(log n)

---

## 🔹 1. Exact Match

Used when we need to find a target element.

```python 

while left <= right:
    mid = (left + right) // 2
    
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1