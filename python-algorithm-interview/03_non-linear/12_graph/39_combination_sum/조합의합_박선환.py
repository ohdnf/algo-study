class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        L = len(candidates)
        result = []
        
        def dfs(i, current=[]):
            if sum(current) >= target:
                if sum(current) == target:
                    result.append(current)
                return
            for j in range(i, L):
                dfs(j, current + [candidates[j]])
        dfs(0)
        
        return result