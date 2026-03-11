class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result


if __name__ == "__main__":
    nums = [1,2,2,3,1]
    s = Solution()
    print(s.singleNumber(nums))