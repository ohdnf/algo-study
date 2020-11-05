class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs(n, lst):
            if n == len(nums):
                result.append(lst)
            else:
                dfs(n+1, lst + [nums[n]])
                dfs(n+1, lst[:])
        
        dfs(0, [])
        return result
# 32 ms	14.3 MB	python3
'''
# 책에 나온 코드 => 각각의 트리 형식
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs(n, lst):
            result.append(lst)
            for i in range(n, len(nums)):
                dfs(i+1, lst + [nums[i]])
        
        dfs(0, [])
        return result
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        import itertools
        result = []
        for n in range(len(nums)+1):
            result.extend(list(map(list, itertools.combinations(nums, n))))
        return result
# 32 ms	14.1 MB	python3
'''