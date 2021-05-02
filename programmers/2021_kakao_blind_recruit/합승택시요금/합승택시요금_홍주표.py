from collections import defaultdict, deque

def solution_failed_1(n, s, a, b, fares):
    # 택시요금 dictionary화
    graph = defaultdict(dict)
    nodes = set()
    for c, d, f in fares:
        graph[c][d] = f
        graph[d][c] = f
        nodes.add(c)
        nodes.add(d)
    # 합승했을 경우 시작지점에서 합승 지점까지 최단거리 요금 계산
    checkpoints = {node: float('inf') for node in nodes}
    checkpoints[s] = 0
    checked = {node: False for node in nodes}
    queue = deque()
    queue.append((s, 0))
    while queue:
        curr_node, curr_cost = queue.popleft()
        checked[curr_node] = True
        for next_node, next_cost in graph[curr_node].items():
            if not checked[next_node]:
                checkpoints[next_node] = min(checkpoints[next_node], curr_cost + next_cost)
                queue.append((next_node, curr_cost + next_cost))
    # 각 합승 지점에서 두 사람이 각자 집까지 최단거리 요금 계산
    def dijkstra(dep, arr):
        costs = {node: float('inf') for node in nodes}
        costs[dep] = 0
        visited = {node: False for node in nodes}
        queue = deque()
        queue.append((dep, 0))
        while queue:
            curr_node, curr_cost = queue.popleft()
            visited[curr_node] = True
            for next_node, next_cost in graph[curr_node].items():
                if not visited[next_node]:
                    costs[next_node] = min(costs[next_node], curr_cost + next_cost)
                    queue.append((next_node, curr_cost + next_cost))
        return costs[arr]

    for checkpoint, start_cost in checkpoints.items():
        checkpoints[checkpoint] = start_cost + dijkstra(checkpoint, a) + dijkstra(checkpoint, b)
    
    return min(checkpoints.values())


def solution(n, s, a, b, fares):
    # Using Floyd-Warshall Algorithm
    dist = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        dist[i][i] = 0

    for c, d, f in fares:
        dist[c][d] = f
        dist[d][c] = f

    for k in range(1, n+1):
        for i in range(1, n+1):
            if i != k:
                for j in range(1, n+1):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    answer = dist[s][a] + dist[s][b]
    for k in range(1, n+1):
        answer = min(answer, dist[s][k] + dist[k][a] + dist[k][b])
    
    return answer

"""
정확성  테스트
테스트 1 〉	통과 (0.13ms, 10.3MB)
테스트 2 〉	통과 (0.18ms, 10.3MB)
테스트 3 〉	통과 (0.13ms, 10.3MB)
테스트 4 〉	통과 (0.51ms, 10.3MB)
테스트 5 〉	통과 (0.87ms, 10.3MB)
테스트 6 〉	통과 (1.24ms, 10.3MB)
테스트 7 〉	통과 (1.00ms, 10.3MB)
테스트 8 〉	통과 (1.66ms, 10.3MB)
테스트 9 〉	통과 (2.80ms, 10.3MB)
테스트 10 〉	통과 (3.17ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (294.25ms, 10.4MB)
테스트 2 〉	통과 (1017.11ms, 11.2MB)
테스트 3 〉	통과 (2345.80ms, 11.7MB)
테스트 4 〉	통과 (2311.09ms, 11.5MB)
테스트 5 〉	통과 (2317.46ms, 11.5MB)
테스트 6 〉	통과 (2345.75ms, 11.6MB)
테스트 7 〉	통과 (2281.91ms, 14.2MB)
테스트 8 〉	통과 (2335.40ms, 14.1MB)
테스트 9 〉	통과 (2548.40ms, 14.1MB)
테스트 10 〉	통과 (2269.89ms, 14.1MB)
테스트 11 〉	통과 (2520.61ms, 14.2MB)
테스트 12 〉	통과 (2252.63ms, 12.8MB)
테스트 13 〉	통과 (2313.19ms, 12.8MB)
테스트 14 〉	통과 (2228.71ms, 12.8MB)
테스트 15 〉	통과 (2272.72ms, 12.8MB)
테스트 16 〉	통과 (2331.23ms, 11.3MB)
테스트 17 〉	통과 (2216.72ms, 11.4MB)
테스트 18 〉	통과 (2361.69ms, 11.5MB)
테스트 19 〉	통과 (2260.88ms, 11.7MB)
테스트 20 〉	통과 (2454.62ms, 11.8MB)
테스트 21 〉	통과 (2500.18ms, 11.7MB)
테스트 22 〉	통과 (2221.95ms, 12.7MB)
테스트 23 〉	통과 (2341.89ms, 12.9MB)
테스트 24 〉	통과 (2447.49ms, 12.9MB)
테스트 25 〉	통과 (2211.63ms, 11.7MB)
테스트 26 〉	통과 (2229.77ms, 11.6MB)
테스트 27 〉	통과 (2110.77ms, 11.6MB)
테스트 28 〉	통과 (2209.83ms, 11.7MB)
테스트 29 〉	통과 (303.40ms, 10.6MB)
테스트 30 〉	통과 (281.89ms, 10.5MB)
"""