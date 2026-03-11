class Solution :
    def singleNumber(self, nums) :
        result = 0
        for num in nums:
            result ^= num

        return result

S = Solution()
nums = [1,2,2,3,1]
print(S.singleNumber(nums))
