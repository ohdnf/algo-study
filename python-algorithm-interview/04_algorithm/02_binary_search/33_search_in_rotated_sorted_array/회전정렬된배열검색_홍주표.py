class Solution:
    def bin_search(self, arr: List[int], target: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > target:
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        cut = -1
        for idx in range(1, len(nums)):
            if nums[idx-1] > nums[idx]:
                cut = idx
                break
        
        if cut != -1:
            left_nums = nums[:idx]
            right_nums = nums[idx:]
            left_idx = self.bin_search(left_nums, target)
            right_idx = self.bin_search(right_nums, target)
            if left_idx != -1:
                return left_idx
            elif right_idx != -1:
                return right_idx + idx

            else:
                return -1
            
        return self.bin_search(nums, target)


"""
Runtime: 44 ms, faster than 50.65% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 14.8 MB, less than 24.57% of Python3 online submissions for Search in Rotated Sorted Array.
"""
