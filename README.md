# Coding Practice

## Project Description

This repository contains my daily coding practice as part of my journey toward becoming a Machine Learning Engineer and Software Engineer.

The goal of this repository is to improve problem solving skills, strengthen understanding of Data Structures and Algorithms, and maintain consistent coding practice while preparing for technical interviews.

All solutions and learning notes are organized to track my daily progress and learning journey.

---
## Goals

- Strengthen Data Structures and Algorithms knowledge
- Practice Git and GitHub workflow used in real development
- Prepare for Software Engineering and AI/ML interviews
- Build a consistent daily coding habit

## Repository Structure

```
coding-practice/
│
├── leetcode/
│   ├── problem_name.py
│
├── notes/
│   ├── note.md
│
└── README.md
```

- **leetcode/** → contains solutions to LeetCode problems  
- **notes/** → contains notes about Git, programming concepts, and learning progress  

---

## Example Problem

Example: Two Sum

### Input
```
nums = [2,7,11,15]
target = 9
```

### Output
```
[0,1]
```

### Explanation

The numbers at index **0** and **1** add up to the target value.

---

## Day 1

- Learned basic Git workflow
- Created repository structure
- Solved LeetCode problem: Single Number

## Day 2

- Learned Git push and Git pull commands
- Solved LeetCode problem: Move Zeroes
- Solved LeetCode problem: Maximum Subarray
- Studied array traversal concepts
- Practiced committing and pushing code to GitHub

## Day 3

### Git
Learned how to clone a repository using:

git clone

### LeetCode Problems
1. Valid Palindrome
2. Reverse String

### Concepts Learned
- String manipulation
- isalnum()
- lower()
- string slicing
- two pointer technique

## Day 4

### Topics Learned:
- Git branching
- git branch
- git checkout
- Feature branch workflow

### Coding Practice:
- Two Sum II (Two Pointer technique)
- Squares of a Sorted Array

### Notes:
- Two Pointer algorithm pattern

## Day 5

### Topics Learned:
- Git merge
- Branch merging workflow
- Frequency counting technique

### Git Commands Practiced:
- git merge
- git checkout
- git branch

### LeetCode Problems:
- Majority Element
- Missing Number

### Notes:
- frequency_counting.md

## Day 6
### Focus:
Improving GitHub repository quality and strengthening array problem solving skills.

### Tasks Completed:
- Solved two LeetCode problems
- Studied common array problem solving patterns
- Documented array patterns in notes
- Continued building a consistent coding practice repository

### 
Key Idea:
Maintaining a clean repository and documenting concepts improves both understanding and professionalism. Consistency in daily coding practice helps develop stronger problem solving skills over time.

## Day 7

### Focus:
Reviewing Git commands and verifying repository commits.

### Tasks Completed:
- Reviewed important Git commands
- Checked commit history using `git log`
- Verified repository status using `git status`
- Continued maintaining daily coding discipline

### Key Idea:
Regular review of Git commands strengthens version control skills and ensures consistent repository management.

## Day 8

---

### ✅ Problems Solved
- Valid Anagram → HashMap (Frequency Count)
- Merge Sorted Array → Two Pointers

---

### 🧠 Concepts Learned
- Frequency Counting using HashMap
- Two Pointer Technique
- In-place array manipulation

---

### 💡 Key Takeaways
- Counting is more efficient than sorting for comparison problems
- Two pointer approach helps reduce extra space
- Always think about optimizing time complexity

---

### 🚀 Progress Update
Focused on strengthening fundamental problem-solving patterns and writing clean, structured code.

---

### 📂 Files Added
- `valid_anagram.py`
- `merge_sorted_array.py`
- `patterns.md`


---

## Day 9 - Hash Map Pattern

### Solved Problems:
- Intersection of Two Arrays II
- Find the Difference

### Concepts Learned:
- Frequency map for comparing arrays
- Hash map pattern
- XOR optimization technique

### Status: Completed ✅

---

##  Day 10

---

### 🧩 Problems Solved
- Reverse Words in a String → String Manipulation (Split + Reverse)
- First Unique Character in String → HashMap (Frequency Count + Two Pass)

---

### 🧠 Concepts Learned
- String traversal techniques
- Word-based string manipulation
- Two-pass algorithm approach
- Frequency counting using HashMap

---

### 💡 Key Takeaways
- Always preprocess strings (strip, split) before solving
- Two-pass approach simplifies decision-making problems
- HashMaps are essential for frequency-based questions
- Clean code is better than clever one-liners in interviews

---

### 🚀 Progress Update
Focused on strengthening string problem-solving patterns and improving understanding of traversal logic.

---

### 📁 Files Added
- reverse_words_in_a_string.py
- first_unique_character_in_string.py
- notes/string_traversal_logic.md

---
## Day 11 - Binary Search

### 📚 Topics Covered
- Binary Search Algorithm
- Searching in a sorted array
- Two-pointer technique (left, right, mid)

### 💻 LeetCode Problems
1. Binary Search

### 🧠 Key Learnings
- Binary search works only on sorted arrays
- Reduces search space by half each iteration
- Time complexity: O(log n)
- Importance of correct loop condition (left <= right)

### 📁 Files Added
- leetcode/binary_search.py
- notes/binary_search.md

---

## 📅 Day 12 – Binary Search Variations

### 📚 Topics Covered
- Binary Search (Advanced Patterns)
- Search Insert Position
- First Bad Version (Boundary Problem)
- Understanding left and right boundaries

---

### 💻 LeetCode Problems
1. Search Insert Position  
2. First Bad Version  

---

### 🧠 Key Learnings
- Binary search is not just for exact match problems
- Learned how to find insertion position using `left`
- Understood boundary-based search (first true condition)
- Difference between:
  - `left <= right` (exact match)
  - `left < right` (boundary problems)
- Importance of:
  - `right = mid` vs `right = mid - 1`

---

### 📁 Files Added
- leetcode/search_insert_position.py
- leetcode/first_bad_version.py
- notes/binary_search_variations.md

---

### 🚀 Progress Insight
Improved understanding of binary search patterns and how to apply them in different problem types.

## 📅 Day 13 - In-place & Prefix Patterns

### 📌 Problems Solved
- Remove Duplicates from Sorted Array  
- Product of Array Except Self  

### 🧠 Concepts Learned
- Two Pointers (in-place array modification)  
- Prefix & Suffix Product Pattern  
- Space Optimization Techniques  

### 🚀 Key Takeaways
- Learned how to modify arrays without extra space  
- Understood prefix-suffix logic deeply  
- Improved optimization thinking  

### 📂 Files
- `leetcode/remove_duplicates_sorted_array.py`  
- `leetcode/product_of_array_except_self.py`  
- `notes/inplace-and-prefix-patterns.md`