class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        
        return -1

"""
Runtime: 232 ms, faster than 83.84% of Python3 online submissions for Binary Search.
Memory Usage: 15.6 MB, less than 32.83% of Python3 online submissions for Binary Search.
"""
