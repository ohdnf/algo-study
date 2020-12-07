class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        G = collections.defaultdict(list)
        # G = [ [0] * n for _ in range(n)]
        for a, b in edges:
            G[a].append(b)
            G[b].append(a)
        leaves = []
        for node, nodes in G.items():
            if len(nodes) == 1: # leaf Node는 길이가 1
                leaves.append(node)
        if not leaves: # 예외 케이스 처리
            return list(range(n))
        leaves_cnt = 0
        while True:
            leaves_cnt += len(leaves)
            if leaves_cnt == n: # 정답
                return leaves
            next_leaves = []
            for leaf in leaves:
                w = G[leaf][0]
                G[w].remove(leaf) # 길이가 >=2 였지만, 이 동작에 의해 길이가 <= 1이 되면 next_leaves에 추가
                G[leaf] = []
                if len(G[w]) == 1:
                    next_leaves.append(w)
            leaves = next_leaves

'''
Runtime: 228 ms, faster than 79.81% of Python3 online submissions for Minimum Height Trees.
Memory Usage: 18 MB, less than 94.01% of Python3 online submissions for Minimum Height Trees.
'''