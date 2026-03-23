# Binary Search Notes

## When to Use
- Array must be sorted

## Time Complexity
- O(log n)

## Logic
- Use two pointers: left and right
- Find mid index
- Compare target with mid
- Reduce search space by half

## Template
```python
while left <= right:
    mid = (left + right) // 2