#  Advanced Easy Patterns

## Problems Solved

### 1. Remove Duplicates from Sorted Array
- Approach: Two pointers (slow & fast)
- Logic:
  - Use one pointer to track position of unique elements
  - Traverse with second pointer
  - Overwrite duplicates in-place
- Time Complexity: O(n)
- Space Complexity: O(1)
- Learning:
  - In-place array modification
  - Pointer coordination is critical

---

### 2. Product of Array Except Self
- Approach: Prefix + Suffix
- Logic:
  - Build prefix product from left
  - Build suffix product from right
  - Multiply both
- Time Complexity: O(n)
- Space Complexity: O(n) → can optimize to O(1)
- Learning:
  - Avoid division
  - Understand prefix-suffix pattern deeply

---

## Mistakes
- (Write honestly, example:)
- Initially confused about pointer movement
- Took time to understand prefix-suffix logic

---

## Improvements
- Better understanding of in-place operations
- Improved thinking for optimization problems