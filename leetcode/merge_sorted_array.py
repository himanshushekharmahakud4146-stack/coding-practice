from typing import List

class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        return nums1

if __name__ == "__main__":
    sol = Solution()
    n1 = [1, 2, 3, 0, 0, 0]
    M = 3
    n2 = [ 2, 3, 6]
    N = 3
    print(sol.merge(n1, M, n2, N))