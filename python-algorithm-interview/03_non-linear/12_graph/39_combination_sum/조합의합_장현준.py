class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 숫자 중복사용 가능
        
        result = []
        def dfs(n, sums, lst):
            if sums == target and lst not in result: # 정답에 추가
                result.append(lst)
            if n == len(candidates): # 범위 초과
                pass
            else:
                new_lst = lst[:]
                dfs(n+1, sums, new_lst)
                sums += candidates[n]
                while sums <= target:
                    dfs(n+1, sums, new_lst + [candidates[n]])
                    new_lst.append(candidates[n])
                    sums += candidates[n]
        dfs(0, 0, [])
        return result
# 100 ms	14.2 MB	python3
# 순서만 거꾸로 92 ms	14.1 MB	python3
'''
# do-while => while형식으로?
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 숫자 중복사용 가능
        
        result = []
        def dfs(n, sums, origin_lst):
            if sums == target and origin_lst not in result: # 정답에 추가
                result.append(origin_lst)
            if n == len(candidates): # 범위 초과
                pass
            else:
                lst = origin_lst[:]
                while sums <= target:
                    dfs(n+1, sums, lst[:])
                    sums += candidates[n]
                    lst.append(candidates[n])
        dfs(0, 0, [])
        return result
# 120 ms	14.1 MB	python3
# 위 코드에 순서거꾸로 하면 108 ms	14.1 MB	python3
'''