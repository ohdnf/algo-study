def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize:
        for city in cities:
            city = city.lower()
            if not city in cache:
                # cache miss
                answer += 5
                if len(cache) < cacheSize:
                    cache.append(city)
                else:
                    cache.pop(0)
                    cache.append(city)
            else:
                # cache hit
                answer += 1
                cache.pop(cache.index(city))
                cache.append(city)
    else:
        answer = 5*len(cities)
    return answer

'''
정확도 테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.00ms, 10MB)
테스트 7 〉	통과 (0.00ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.07ms, 10.2MB)
테스트 11 〉	통과 (66.01ms, 17.5MB)
테스트 12 〉	통과 (0.05ms, 10.1MB)
테스트 13 〉	통과 (0.09ms, 10.1MB)
테스트 14 〉	통과 (0.13ms, 10.3MB)
테스트 15 〉	통과 (0.21ms, 10.2MB)
테스트 16 〉	통과 (0.26ms, 10.2MB)
테스트 17 〉	통과 (0.00ms, 10.1MB)
테스트 18 〉	통과 (0.66ms, 10.2MB)
테스트 19 〉	통과 (0.89ms, 10.3MB)
테스트 20 〉	통과 (1.09ms, 10.2MB)
'''