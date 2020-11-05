class Solution:
    def subsets(self, nums):
        result = [[]]

        def get_subset(i, target, subset): # i: nums의 인덱스, target: 목표 길이
            if len(subset) == target:
                result.append(subset)
                return
            for index in range(i, len(nums)):
                get_subset(index+1, target, subset+[nums[index]])
        if nums:
            result.append(nums)
            for i in range(1, len(nums)):
                get_subset(0, i, [])
        return result


a = Solution().subsets([1,2,3])