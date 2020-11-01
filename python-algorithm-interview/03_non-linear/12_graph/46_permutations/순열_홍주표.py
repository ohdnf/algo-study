class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        output = []

        def dfs(level, arr):
            if level == len(nums):
                output.append(arr)
            else:
                for idx, num in enumerate(nums):
                    if not used[idx]:
                        used[idx] = True
                        dfs(level + 1, arr + [num, ])
                        used[idx] = False

        dfs(0, [])

        return output
