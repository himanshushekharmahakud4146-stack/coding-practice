from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0 , len(nums) - 1

        while left <= right :
            mid = (left + right) // 2

            if nums[mid] == target :
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
if __name__ == "__main__":
    sol = Solution()
    n = [1,2,3,4,5,6,7,8,9]
    target = 9
    print(sol.search(n, target))