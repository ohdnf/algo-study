# DFS
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def dfs(idx, subset):
            if idx == len(nums):
                subsets.append(subset)
            else:
                dfs(idx + 1, subset + [nums[idx], ])
                dfs(idx + 1, subset)

        dfs(0, [])

        return subsets


# Shift operator
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        for i in range(1 << len(nums)):
            subset = []
            for j in range(len(nums)):
                if i & (1 << j):
                    subset.append(nums[j])
            subsets.append(subset)

        return subsets