class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs(i, current=[]):
            if i >= len(nums):
                result.append(current)
                return
            dfs(i+1, current)
            dfs(i+1, current + [nums[i]])
        dfs(0)
        
        return result