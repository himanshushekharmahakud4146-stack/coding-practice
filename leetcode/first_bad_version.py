# Mock the isBadVersion API for local testing
bad_version = 4  # Suppose version 4 is the first bad one

def isBadVersion(version: int) -> bool:
    return version >= bad_version


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    sol = Solution()
    n = 7
    result = sol.firstBadVersion(n)
    print(f"First bad version: {result}")