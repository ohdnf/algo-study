class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def dfs(idx, lst):
            if len(lst) == k:# k개 모든 고른 경우
                result.append(lst)
            elif (n-idx) + len(lst) < k:# 다 골라도 k가 안되는 경우
                pass
            else:
                dfs(idx+1, lst)
                dfs(idx+1, lst+[idx+1])
        dfs(0, [])
        return result
# 84 ms	15.5 MB	python3
'''
# 책 코드를 참조한 버전
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        def dfs(start, remain, lst):
            if len(lst) == k: # k개 고른 경우
                result.append(lst)
            elif (n - start) + len(lst) < k: # 모두 골라도 k개가 안 되는 경우
                pass
            else:
                for i in range(start+1, n+1):
                    dfs(i, k-1, lst+[i])
        dfs(0, k, [])
        return result
# 96 ms	15.6 MB	python3

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        import itertools
        return list(itertools.combinations( (range(1,n+1)), k))
# 76 ms	15.3 MB	python3
'''