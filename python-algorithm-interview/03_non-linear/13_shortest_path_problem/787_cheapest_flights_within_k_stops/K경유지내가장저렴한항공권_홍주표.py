class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        tickets = collections.defaultdict(list)
        for u, v, w in flights:
            tickets[u].append((v, w))

        cheapest_price = [float('inf')] * n

        queue = collections.deque()
        queue.append((src, 0, 0))

        while queue:
            departure, cur_cost, stops = queue.popleft()

            if stops > K:
                continue

            for arrival, price in tickets[departure]:
                if cheapest_price[arrival] > price + cur_cost:
                    cheapest_price[arrival] = price + cur_cost
                    queue.append((arrival, price + cur_cost, stops + 1))

        return cheapest_price[dst] if cheapest_price[dst] < float('inf') else -1

"""
Runtime: 72 ms, faster than 98.39% of Python3 online submissions for Cheapest Flights Within K Stops.
Memory Usage: 14.9 MB, less than 6.38% of Python3 online submissions for Cheapest Flights Within K Stops.
"""
