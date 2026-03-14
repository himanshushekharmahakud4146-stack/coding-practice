from typing import List


class Solution:
    def twosum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return []
if __name__ == "__main__":
    sol = Solution()
    num = [2, 7, 11, 15]
    tar = 9
    print(sol.twosum(num, tar))