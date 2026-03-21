# Hash Map Pattern

## What is Hash Map?
A hash map stores data in key-value pairs and allows fast lookup in O(1) time.

---

## When to Use
- Counting frequency
- Finding duplicates
- Comparing two datasets
- Checking existence

---

## Common Problems
- Two Sum
- Valid Anagram
- Intersection of Two Arrays II
- Find the Difference

---

## Template Code

```python
freq = {}

for item in arr:
    freq[item] = freq.get(item, 0) + 1