from typing import List

class Solution:
    def generate(self,numRows : int) -> List[List[int]]:
        triangle = []  # This will hold all rows

        for i in range(numRows):  # Loop: once for each row (0, 1, 2, ...)
            row = [1] * (i + 1)  # Create a row filled with 1s
            # Row 0 → [1], Row 1 → [1,1], Row 2 → [1,1,1]

            for j in range(1, i):  # Fill MIDDLE numbers only (skip index 0 and last)
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
                #         ↑ number to upper-left    ↑ number to upper-right

            triangle.append(row)  # Add completed row to result

        return triangle

if __name__ == "__main__":
    sol = Solution()
    numRows = 5
    print(sol.generate(numRows))