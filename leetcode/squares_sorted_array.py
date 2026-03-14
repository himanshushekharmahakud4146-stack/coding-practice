from typing import List

class Solution:
    def sortedsquares(self, num: List[int]) -> List[int]:
        left , right = 0 , len(num) - 1
        result = [0] * len(num)
        pos = right

        while left <= right:
            if abs(num[left]) > abs(num[right]):
                result[pos] = num[left] ** 2
                left += 1
            else:
                result[pos] = num[right] ** 2
                right -= 1

            pos -= 1

        return result

if __name__ == "__main__":
    nums = [-4, -3, 0, 3, 5, 7, 9, ]
    sol = Solution()
    print(sol.sortedsquares(nums))