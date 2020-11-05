class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [0] * len(nums)
        result = []
        def dfs(lst):
            if len(lst) == len(nums):
                result.append(lst)
            else:
                for i in range(len(nums)):
                    if not used[i]:
                        used[i] = 1
                        dfs(lst + [nums[i]])
                        used[i] = 0
        dfs([])
        return result
# 40 ms	14.2 MB	python3
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        import itertools
        return list(map(list, itertools.permutations(nums)))
        # 36 ms	14.1 MB	python3

        # return list(itertools.permutations(nums))
        # 32 ms	14.1 MB	python3
'''