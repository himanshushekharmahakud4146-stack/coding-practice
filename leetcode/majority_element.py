from typing import List
from collections import Counter
class Solution:
    def majorityelement(self, nums: List[int]) -> int:
        count = Counter(nums)
        return max(count,key = count.get)

if __name__ == "__main__":
    sol = Solution()
    num = [2,2,1,1,1,2,2]
    print(sol.majorityelement(num))