class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num1 in nums1:
            for num2 in nums2:
                if num1 == num2 and num1 not in result:
                    result.append(num1)
        return result

"""
Runtime: 140 ms, faster than 5.09% of Python3 online submissions for Intersection of Two Arrays.
Memory Usage: 14.4 MB, less than 75.96% of Python3 online submissions for Intersection of Two Arrays.
"""
