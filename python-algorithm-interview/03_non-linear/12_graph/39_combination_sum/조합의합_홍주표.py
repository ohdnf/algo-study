# 첫 풀이
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = set()

        def dfs(idx, combi):
            if idx == len(candidates):
                return
            curr = sum(map(int, combi.split()))
            if curr == target:
                result.add(combi)
                return
            elif curr > target:
                return
            else:
                dfs(idx, combi + str(candidates[idx]) + " ")
                dfs(idx + 1, combi)

        dfs(0, "")

        output = [list(map(int, nums.split())) for nums in result]

        return output

# 수정한 풀이

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = list()

        def dfs(idx, combi):
            curr = sum(combi)
            if idx == len(candidates):
                if curr == target:
                    result.append(combi[:])
                return

            if curr == target:
                result.append(combi[:])
                return
            elif curr > target:
                return
            else:
                dfs(idx, combi + [candidates[idx], ])
                dfs(idx + 1, combi)

        dfs(0, [])

        return result

# 더 나은 풀이

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(target, curr, combi):
            if target < 0:
                return
            elif target == 0:
                result.append(combi)
                return
            else:
                for idx in range(curr, len(candidates)):
                    dfs(target - candidates[idx], idx, combi + [candidates[idx], ])

        dfs(target, 0, [])

        return result
