from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1

if __name__ == "__main__":
    nums = [0, 1, 0, 3, 2, 4, 5, 6, 0, 0, 0]
    sol = Solution()
    sol.moveZeroes(nums)
    print(nums)