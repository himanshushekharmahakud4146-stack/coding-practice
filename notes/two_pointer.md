# Two Pointer Technique

The two pointer technique is an algorithm pattern used mainly on arrays.

Instead of using nested loops (O(n²)), two indices move through the array to reduce time complexity to O(n).

## Basic Idea

Two pointers start at different positions.

Example:
left = start of array  
right = end of array

Move the pointers depending on the condition.

## When to Use

The two pointer technique is useful when:

- The array is sorted
- We need to find pairs
- We process elements from both ends

## Example Problems

1. Two Sum II
2. Squares of a Sorted Array

## Example Logic

left = 0  
right = len(array) - 1

while left < right:

- if condition satisfied → return result
- if value too small → move left++
- if value too big → move right--

Time Complexity: O(n)
Space Complexity: O(1)