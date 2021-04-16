# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         for i in range(len(numbers) - 1):
#             if numbers[i] + numbers[-1] < target:
#                 continue
#             for j in range(i + 1, len(numbers)):
#                 if numbers[i] + numbers[j] == target:
#                     return [i + 1, j + 1]

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx in range(len(numbers) - 1):
            temp = target - numbers[idx]
            left = idx + 1
            right = len(numbers) - 1
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] < temp:
                    left = mid + 1
                elif numbers[mid] > temp:
                    right = mid - 1
                else:
                    return [idx + 1, mid + 1]

"""
Runtime: 84 ms, faster than 14.63% of Python3 online submissions for Two Sum II - Input array is sorted.
Memory Usage: 14.7 MB, less than 59.04% of Python3 online submissions for Two Sum II - Input array is sorted.
"""