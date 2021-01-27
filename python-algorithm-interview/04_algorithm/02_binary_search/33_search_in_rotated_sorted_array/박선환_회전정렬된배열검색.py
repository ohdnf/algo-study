class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_index = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[min_index]:
                min_index = i
        nums = nums[min_index:] + nums[:min_index]
        
        li, ri = 0, len(nums) - 1
        result = -1
        while ri >= li:
            center = (li+ri)//2
            if nums[center] == target:
                result = center
                break
            elif nums[center] > target:
                ri = center - 1
            elif nums[center] < target:
                li = center + 1
        if result == -1:
            return result
        elif result >= len(nums) - min_index:
            return result - (len(nums) - min_index)
        else:
            return result + min_index

'''
Runtime: 52 ms, faster than 11.29% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 14.7 MB, less than 56.20% of Python3 online submissions for Search in Rotated Sorted Array.
'''