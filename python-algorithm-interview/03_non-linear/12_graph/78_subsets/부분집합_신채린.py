class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(depth, arr):
            if depth == len(nums):
                answer.append(arr)
                return
            else:
                dfs(depth + 1, arr + [nums[depth]])
                dfs(depth + 1, arr)
        answer = []
        dfs(0, [])
        return answer