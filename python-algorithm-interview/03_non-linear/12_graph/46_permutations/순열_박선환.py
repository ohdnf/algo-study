class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        L = len(nums)
        visited = [0]*L
        result = []
        
        def dfs(index, current=[]):
            if index == L:
                result.append(current)
                return
            for i in range(L):
                if not visited[i]:
                    visited[i] = 1
                    dfs(index + 1, current + [nums[i]])
                    visited[i] = 0
        dfs(0)
        
        return result