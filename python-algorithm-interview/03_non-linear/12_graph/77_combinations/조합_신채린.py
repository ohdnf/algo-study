class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        
        def dfs(start_num, depth, comb):
            if depth == k:
                answer.append(comb)
            for num in range(start_num + 1, n + 1):
                dfs(num, depth + 1, comb + [num])
       
        dfs(0, 0, [])
        
        return answer