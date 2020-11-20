class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        
        for u, v, w in flights:
            graph[u].append((v, w))
        
        q = [(0, src, K)]
        
        while q:
            price, node, k = heapq.heappop(q)
            if node == dst:
                return price
            if k >= 0: 
                for v, w in graph[node]:
                    alt = price + w
                    heapq. heappush(q, (alt, v, k - 1))
        return -1
