class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []

        def dfs(start_num: int, level: int, combi: List[int]):
            if level == k:
                answer.append(combi)
            else:
                for num in range(start_num + 1, n + 1):
                    dfs(num, level + 1, combi + [num, ])

        dfs(0, 0, [])

        return answer
