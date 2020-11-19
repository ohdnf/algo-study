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

# 아래
# Runtime: 488 ms, faster than 47.21% of Python3 online submissions for Network Delay Time.
# Memory Usage: 16.1 MB, less than 20.68% of Python3 online submissions for Network Delay Time.

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        INF = float('inf')
        G = dict()
        for u, v, w in times:
            if u in G:
                G[u].append((v, w))
            else:
                G[u] = [(v, w)]
        
        import heapq
        q = []
        dist = dict()
        heapq.heappush(q, (0, K))
        while q:
            price, node = heapq.heappop(q)
            if node in dist: continue
            dist[node] = price # 최소비용순으로 꺼내기때문에, 첫 방문했다면 무조건 최저값이다.
            if node not in G: continue # 일반 dict는 검사해야한다. 책의 defaultdict는 넘어간다.
            for w, cost in G[node]:
                heapq.heappush(q, (price + cost, w))
        if len(dist) == N:
            return max(dist.values())
        else:
            return -1

# 책의 collections.defaultdict(list) 사용시
# Runtime: 480 ms, faster than 51.18% of Python3 online submissions for Network Delay Time.
# Memory Usage: 15.9 MB, less than 46.42% of Python3 online submissions for Network Delay Time.