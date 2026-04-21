from typing import List
class Solution:
    def product_except_self(self,nums:List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]

        right = 1
        for i in range(n-1, -1, -1):
            answer[i] = answer[i] * right
            right *= nums[i]

        return answer

if __name__ ==  "__main__":
    s = Solution()
    print(s.product_except_self([1,2,3,4]))
    print(s.product_except_self([-1,1,0,-3,3]))
