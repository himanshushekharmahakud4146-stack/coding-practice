from typing import List
class Solution:
    def containsduplicate(self, nums: List[int]) -> bool:
        if len(nums) != len(set(nums)):
            return True
        return False

if __name__ == "__main__":
    sol = Solution()
    n = [1,2,3,1]
    print(sol.containsduplicate(n))