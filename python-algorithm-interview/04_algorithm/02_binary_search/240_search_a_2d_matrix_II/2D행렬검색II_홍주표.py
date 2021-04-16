from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            left = 0
            right = len(matrix[row]) - 1
            while left <= right:
                mid = (left + right) // 2
                if matrix[row][mid] < target:
                    left = mid + 1
                elif matrix[row][mid] > target:
                    right = mid - 1
                else:
                    return True
        return False

"""
Runtime: 176 ms, faster than 21.89% of Python3 online submissions for Search a 2D Matrix II.
Memory Usage: 20.6 MB, less than 66.50% of Python3 online submissions for Search a 2D Matrix II.
"""