from collections import deque as dq


def solution(cache_size, cities):
    answer = 0
    cache = dq()

    if cache_size == 0:
        return 5 * len(cities)

    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            if len(cache) == cache_size:
                # Remove the least recently used item
                cache.popleft()
            cache.append(city)
    return answer

"""
정확성 테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.00ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.05ms, 10.2MB)
테스트 11 〉	통과 (69.94ms, 17.5MB)
테스트 12 〉	통과 (0.04ms, 10.2MB)
테스트 13 〉	통과 (0.09ms, 10.2MB)
테스트 14 〉	통과 (0.14ms, 10.2MB)
테스트 15 〉	통과 (0.20ms, 10.2MB)
테스트 16 〉	통과 (0.25ms, 10.2MB)
테스트 17 〉	통과 (0.00ms, 10.2MB)
테스트 18 〉	통과 (0.66ms, 10.3MB)
테스트 19 〉	통과 (0.92ms, 10.2MB)
테스트 20 〉	통과 (1.13ms, 10.2MB)
"""