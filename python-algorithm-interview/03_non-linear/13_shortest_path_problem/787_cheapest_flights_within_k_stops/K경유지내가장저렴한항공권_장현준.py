class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        import heapq
        
        # n: 노드수
        # flights: 간선
        # src: 시작노드
        # dst: 목적지 노드
        # K: 경유 노드수
        
        # Q에 들어갈 요소
            # 1. 현재 코스트
            # 2. 현재 노드
            # 3. 현재 경유한 횟수
            
            
        # 다음 탐색시
            # 1. 현재 코스트 + 요금 (우선순위 큐니까 비교는 안해도 될듯?)
            # 2. 현재 노드에 붙어 있는 노드중
            # 3. 경유한 횟수 +1
            
        # 그래프 생성
        G = dict() # G: graph
        for s, d, c in flights:
            # s:src, d:dst, c:cost
            if s in G:
                G[s].append((d, c)) # 다음 노드, 코스트
            else:
                G[s] = [(d, c)]
                
        # 시작 노드
        q = [(0, src, 0)] # 코스트, 현재 노드, 경유 횟수
        
        while q:
            price, v, stops = heapq.heappop(q)
            if stops > K+1: continue; # 제한조건 초과
            if v == dst: return price # 최저가 탐색 완료
            if v not in G: continue; # 탐색한 다음 노드가 없음
            for d, c in G[v]:
                heapq.heappush(q, (price + c, d, stops+1))
        return -1 # 불가능함

# Runtime: 92 ms, faster than 60.87% of Python3 online submissions for Cheapest Flights Within K Stops.
# Memory Usage: 19.6 MB, less than 43.77% of Python3 online submissions for Cheapest Flights Within K Stops.
