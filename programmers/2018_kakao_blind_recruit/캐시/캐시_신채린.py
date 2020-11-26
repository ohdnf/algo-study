from collections import deque
def solution(cacheSize, cities):
    cache = deque()
    time = 0
    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:
        city = city.lower()
        if city in cache:
            time += 1
            cache.remove(city)
            cache.append(city)
        else:
            time += 5
            if len(cache) == cacheSize:
                cache.popleft()
            cache.append(city)
    return time

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.00ms, 10.2MB)
# 테스트 7 〉	통과 (0.00ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)
# 테스트 9 〉	통과 (0.01ms, 10.2MB)
# 테스트 10 〉	통과 (0.05ms, 10.2MB)
# 테스트 11 〉	통과 (70.07ms, 17.6MB)
# 테스트 12 〉	통과 (0.04ms, 10.2MB)
# 테스트 13 〉	통과 (0.09ms, 10.2MB)
# 테스트 14 〉	통과 (0.13ms, 10.2MB)
# 테스트 15 〉	통과 (0.19ms, 10.2MB)
# 테스트 16 〉	통과 (0.25ms, 10.2MB)
# 테스트 17 〉	통과 (0.00ms, 10.3MB)
# 테스트 18 〉	통과 (0.64ms, 10.1MB)
# 테스트 19 〉	통과 (0.88ms, 10.2MB)
# 테스트 20 〉	통과 (1.06ms, 10.2MB)
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0