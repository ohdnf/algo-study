class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
        return result

'''
Runtime: 228 ms, faster than 92.90% of Python3 online submissions for Binary Search.
Memory Usage: 15.6 MB, less than 31.63% of Python3 online submissions for Binary Search.
'''