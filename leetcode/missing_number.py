from typing import List
class Solution:
    def missingnumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n*(n+1)//2
        return expected_sum - sum(nums)

if __name__ == "__main__":
    sol = Solution()
    num =  [9,6,4,2,3,5,7,0,1]
    print(sol.missingnumber(num))