# Pascal's Triangle Notes

## 📌 Problem Summary

Generate Pascal’s Triangle for a given number of rows.

Example:

```text
[
 [1],
 [1,1],
 [1,2,1],
 [1,3,3,1]
]
```

---

## 🧠 Key Concepts Learned

- Nested loops
- List creation
- List indexing
- Building rows dynamically
- Using previous row values
- Pattern recognition

---

## 📖 Important Logic

Each middle value is calculated using:

```python
triangle[i-1][j-1] + triangle[i-1][j]
```

Meaning:

```text
upper-left + upper-right
```

---

## 📌 Example

Previous row:

```text
[1, 1]
```

New row starts as:

```text
[1, 1, 1]
```

Middle value:

```text
1 + 1 = 2
```

Final row:

```text
[1, 2, 1]
```

---

## 🚀 What I Learned

- How nested lists work
- How append() stores rows
- How previous rows help generate new rows
- Basic dynamic programming style thinking

---

## 📂 File

```text
leetcode/pascals_triangle.py
```