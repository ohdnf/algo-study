class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n+1))
        result = []
        
        def dfs(i, current=[]):
            if len(current) == k:
                result.append(current)
                return
            if k + i > len(current) + n:
                return
            dfs(i+1, current + [nums[i]])
            dfs(i+1, current)
        dfs(0)
        
        return result