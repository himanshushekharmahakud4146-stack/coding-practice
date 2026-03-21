

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0

        for ch in s + t:
            result ^= ord(ch)

        return chr(result)

sol = Solution()
sr = "abcd"
tr = "abcde"
print(sol.findTheDifference(sr,tr))