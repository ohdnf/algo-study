"""
결국 혼자 해결하지 못하고 검색 찬스를 사용하였습니다.
알고리즘 고수가 되는 길은 멀고도 험하다는 생각이 듭니다.
로직을 참고하더라도 최대한 외우지 않고 이해하면서 코드를 구현하려 노력했습니다.

두 가지 방법으로 풀 수 있다는 것을 알게 되었습니다.

1. 우선순위 큐 활용
2. 이분탐색
"""

# 우선순위 큐 활용
import heapq as hq

def solution(food_times, k):
    """
    1. 우선순위 큐 풀이 참고
    https://www.youtube.com/watch?v=Rgw0fo6isUM&t=1036s
    2. 파이썬에서는 PriorityQueue보다는 heapq를 사용하는 것이 더 빠르다고 합니다.
    https://stackoverflow.com/questions/36991716/whats-the-difference-between-heapq-and-priorityqueue-in-python
    """
    if sum(food_times) <= k:
        return -1
    
    # 우선순위 큐를 사용하여 제일 적은 음식 섭취 소요시간을 차례로 가져올 수 있게 합니다.
    queue = []
    for idx, time in enumerate(food_times):
        hq.heappush(queue, (time, idx + 1))
    remain, elapsed, before = len(queue), 0, 0
    # 가장 적은 섭취 시간(queue[0][0])을 현재 남아있는 모든 음식의 수(remain)만큼 곱해 총 소요시간에 더할 수 있습니다.
    # 이때 중복 계산을 피하기 위해 직전에 계산했던 섭취 시간(before)만큼을 빼줘야합니다.
    while elapsed + remain * (queue[0][0] - before) <= k:
        now, _ = hq.heappop(queue)
        elapsed += remain * (now - before)
        remain -= 1
        before = now
    # loop를 벗어나고 남은 인덱스를 계산해줍니다.
    queue = sorted(queue, key=lambda q: q[1])
    return queue[(k - elapsed) % remain][1]

"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.1MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.4MB)
테스트 7 〉	통과 (0.02ms, 10.1MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.1MB)
테스트 10 〉	통과 (0.02ms, 9.92MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
테스트 12 〉	통과 (0.02ms, 10.3MB)
테스트 13 〉	통과 (0.02ms, 10.1MB)
테스트 14 〉	통과 (0.02ms, 10.3MB)
테스트 15 〉	통과 (0.02ms, 10.2MB)
테스트 16 〉	통과 (0.00ms, 10.2MB)
테스트 17 〉	통과 (0.02ms, 10.2MB)
테스트 18 〉	통과 (0.03ms, 10.3MB)
테스트 19 〉	통과 (0.00ms, 10.4MB)
테스트 20 〉	통과 (0.00ms, 10.2MB)
테스트 21 〉	통과 (0.15ms, 10.2MB)
테스트 22 〉	통과 (0.17ms, 10.2MB)
테스트 23 〉	통과 (0.00ms, 10MB)
테스트 24 〉	통과 (1.24ms, 10.3MB)
테스트 25 〉	통과 (1.21ms, 10.3MB)
테스트 26 〉	통과 (2.30ms, 10.3MB)
테스트 27 〉	통과 (1.65ms, 10.4MB)
테스트 28 〉	통과 (0.02ms, 10.3MB)
테스트 29 〉	통과 (0.02ms, 10.2MB)
테스트 30 〉	통과 (0.01ms, 10.2MB)
테스트 31 〉	통과 (0.01ms, 10.4MB)
테스트 32 〉	통과 (0.03ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (276.28ms, 42.7MB)
테스트 2 〉	통과 (84.35ms, 42.5MB)
테스트 3 〉	통과 (414.60ms, 39.3MB)
테스트 4 〉	통과 (350.32ms, 39.3MB)
테스트 5 〉	통과 (286.67ms, 42.7MB)
테스트 6 〉	통과 (228.37ms, 43MB)
테스트 7 〉	통과 (289.81ms, 42.2MB)
테스트 8 〉	통과 (175.11ms, 43.5MB)
"""


# 이분탐색 활용
def solution(food_times, k):
    if sum(food_times) < k:
        return -1
    
    lo, hi = 0, 100000000
    N, target, cycle = len(food_times), 0, 0
    
    while lo <= hi:
        # mid = 테이블 회전 수 = 각 음식 섭취 시간에서 감소시킬 시간
        mid = (lo + hi) // 2
        
        # elapsed = mid번 돌았을 때 총 소요 시간
        elapsed = N * mid
        
        # 어떤 음식은 mid보다 작을 수 있기 때문에
        # 다 먹은 후에도 중복해서 시간 누적이 됩니다.
        for time in food_times:
            # 총 섭취 시간에서 중복 시간을 제거해줍니다.
            if time < mid:
                elapsed += time - mid
        
        # k보다 작거나 같은 수 중 최대값을 찾아야 합니다.
        if elapsed <= k:
            target, cycle = elapsed, mid
            lo = mid + 1
        else:
            hi = mid - 1

    # loop를 나와 mid번 회전했을 때 상황을 만들어 줍니다.
    food_times = [time - cycle for time in food_times]
    
    # k초에서 네트워크 장애 발생 -> (idx + 1)번 음식을 다시 섭취합니다.
    for idx, time in enumerate(food_times):
        if time > 0:
            if target == k:
                return idx + 1
            else:
                target += 1
    return -1

"""
정확성  테스트
테스트 1 〉	통과 (0.06ms, 10.2MB)
테스트 2 〉	통과 (0.06ms, 10.2MB)
테스트 3 〉	통과 (0.05ms, 10.2MB)
테스트 4 〉	통과 (0.05ms, 10.3MB)
테스트 5 〉	통과 (0.06ms, 10.2MB)
테스트 6 〉	통과 (0.06ms, 10.2MB)
테스트 7 〉	통과 (0.06ms, 10.2MB)
테스트 8 〉	통과 (0.06ms, 10.2MB)
테스트 9 〉	통과 (0.06ms, 10.2MB)
테스트 10 〉	통과 (0.06ms, 10.1MB)
테스트 11 〉	통과 (0.06ms, 10.1MB)
테스트 12 〉	통과 (0.06ms, 10.2MB)
테스트 13 〉	통과 (0.06ms, 10.2MB)
테스트 14 〉	통과 (0.06ms, 10.1MB)
테스트 15 〉	통과 (0.06ms, 10.2MB)
테스트 16 〉	통과 (0.07ms, 10.2MB)
테스트 17 〉	통과 (0.07ms, 10.3MB)
테스트 18 〉	통과 (0.07ms, 10.1MB)
테스트 19 〉	통과 (0.07ms, 10.2MB)
테스트 20 〉	통과 (0.00ms, 10.2MB)
테스트 21 〉	통과 (0.41ms, 10.2MB)
테스트 22 〉	통과 (0.56ms, 10.1MB)
테스트 23 〉	통과 (0.37ms, 10.2MB)
테스트 24 〉	통과 (3.31ms, 10.1MB)
테스트 25 〉	통과 (3.17ms, 10.2MB)
테스트 26 〉	통과 (4.46ms, 10.3MB)
테스트 27 〉	통과 (3.64ms, 10.3MB)
테스트 28 〉	통과 (0.06ms, 10.1MB)
테스트 29 〉	통과 (0.06ms, 10MB)
테스트 30 〉	통과 (0.02ms, 10.2MB)
테스트 31 〉	통과 (0.02ms, 10.2MB)
테스트 32 〉	통과 (0.10ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (219.10ms, 25.3MB)
테스트 2 〉	통과 (140.09ms, 19.1MB)
테스트 3 〉	통과 (315.48ms, 25.3MB)
테스트 4 〉	통과 (304.30ms, 25.2MB)
테스트 5 〉	통과 (239.69ms, 25.3MB)
테스트 6 〉	통과 (210.89ms, 25MB)
테스트 7 〉	통과 (247.95ms, 25.3MB)
테스트 8 〉	통과 (169.98ms, 25.2MB)
"""
