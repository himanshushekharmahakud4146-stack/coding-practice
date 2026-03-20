
## What is Anagram?

An anagram is when two strings contain the same characters  
with the same frequency, but possibly in different order.

Example:
listen → silent ✅  
rat → car ❌  

---

## What is Valid Anagram?

We check whether two given strings are anagrams or not.

---

## Approach: Frequency Counting (HashMap)

We count how many times each character appears  
in both strings and compare them.

---

## Key Idea

- Same characters  
- Same frequency  
→ Valid Anagram  

---

## Example

Input:
s = "anagram"  
t = "nagaram"  

Output:
True  

---

## Python Implementation

```python
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    count = {}
    
    for char in s:
        count[char] = count.get(char, 0) + 1
    
    for char in t:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
    
    return True