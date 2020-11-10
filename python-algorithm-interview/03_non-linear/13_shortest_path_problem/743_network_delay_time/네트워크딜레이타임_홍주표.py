from typing import List
import collections


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        result = [6000] * N     # 노드별 소요시간
        visited = [False] * N   # 노드별 방문여부

        graph = collections.defaultdict(list)   # 가중치 방향 그래프
        for u, v, w in times:
            graph[u - 1].append((v - 1, w))

        queue = collections.deque()
        queue.append((K - 1, 0))    # 시작 노드
        result[K - 1] = 0

        while queue:
            curr_node, elapsed_time = queue.popleft()
            visited[curr_node] = True

            # 연결된 노드들 탐색
            for next_node, travel_time in graph[curr_node]:
                # 다음 노드의 기존 소요시간이 현재 노드에서 출발해서 도착하는 소요시간보다 길면
                if result[next_node] > travel_time + elapsed_time:
                    result[next_node] = travel_time + elapsed_time  # 소요시간을 변경
                    queue.append((next_node, travel_time + elapsed_time))

        if all(visited):
            return max(result)
        else:
            return -1

"""
Runtime: 432 ms, faster than 95.56% of Python3 online submissions for Network Delay Time.
Memory Usage: 15.7 MB, less than 8.30% of Python3 online submissions for Network Delay Time.
"""
