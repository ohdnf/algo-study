# 일반 큐 사용하는 버전
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        INF = float('inf')
        G = [ list([-1] * (N)) for _ in range(N) ]
        for u, v, w in times:
            G[u-1][v-1] = w #노드 0부터 수정
        K -= 1 # 노드 0부터
        
        from collections import deque 
        q = deque([])
        visited = [INF]*N
        
        cnt = 1
        visited[K] = 0
        q.append(K)
        while q:
            v = q.pop()
            for w in range(N):
                if G[v][w] != -1 and G[v][w] + visited[v] < visited[w]:
                    if visited[w] == INF:
                        cnt += 1
                    visited[w] = G[v][w] + visited[v]
                    q.append(w)
        if cnt == N:
            return max(visited)
        else:
            return -1
# Runtime: 548 ms, faster than 30.13% of Python3 online submissions for Network Delay Time.
# Memory Usage: 15.6 MB, less than 84.04% of Python3 online submissions for Network Delay Time.
# 위
