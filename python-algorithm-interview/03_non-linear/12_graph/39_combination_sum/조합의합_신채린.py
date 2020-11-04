class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(idx, total, arr):
            if idx >= len(candidates):
                return
            if total > target:
                return
            elif total == target:
                answer.append(arr)
                return
            else:
                dfs(idx, total +candidates[idx], arr + [candidates[idx]])
                dfs(idx + 1, total, arr)
        answer = []
        dfs(0, 0, [])
        return answer