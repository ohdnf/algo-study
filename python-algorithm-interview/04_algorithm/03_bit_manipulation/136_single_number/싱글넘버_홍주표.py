from typing import List

class Solution_1:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        answer = -1
        for idx in range(0, len(nums) - 1, 2):
            if nums[idx] != nums[idx + 1]:
                answer = nums[idx]
                break
        else:
            answer = nums[-1]
            
        return answer

"""
Runtime: 132 ms, faster than 65.20% of Python3 online submissions for Single Number.
Memory Usage: 16.6 MB, less than 60.10% of Python3 online submissions for Single Number.
"""


# Implement a solution with a linear runtime complexity and without using extra memory

class Solution_2:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            answer ^= num
        return answer

"""
와 이건 뭐지...
Runtime: 132 ms, faster than 65.20% of Python3 online submissions for Single Number.
Memory Usage: 16.4 MB, less than 98.55% of Python3 online submissions for Single Number.
"""
