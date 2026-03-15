# Frequency Counting

## What is Frequency Counting

Frequency counting is a technique used to count how many times each element appears in a list, array, or string.

It is commonly used in algorithm problems to detect duplicates, find majority elements, or count occurrences.

---

## Example

Input:

[1,2,2,3,3,3]

Frequency:

1 → 1  
2 → 2  
3 → 3

---

## Python Implementation

Using dictionary

```python
nums = [1,2,2,3,3,3]

freq = {}

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)
```
Using Counter
```python
from collections import Counter

nums = [1,2,2,3,3,3]
count = Counter(nums)

print(count)
```