from heapq import heappush, heappop
import copy
def solution(n, s, dst1, dst2, fares):
    
    used = dict()
    
    g = [[] for _ in range(n+1)]
    
    for a, b, cost in fares:
        g[a].append((b, cost))
        g[b].append((a, cost))
    
    h = []
    
    heappush(h, (0, set([s])))
    
    while h:
        paid, path = heappop(h)
        # print(paid, path)
        lst_path = sorted(list(path))
        key = tuple(lst_path)
        if key in used:
            continue
        used[key] = 1
        new_path = set(key)

        # 종료 조건
        if dst1 in path and dst2 in path:
            return paid
        for v in path:
            for w, cost in g[v]:
                if w not in path:
                    key = tuple(sorted(lst_path+[w]))
                    if key in used:
                        continue
                    
                    new_path = copy.copy(path)
                    new_path.add(w)
                    heappush(h, (paid+cost, new_path))
'''
정확성  테스트
테스트 1 〉	통과 (0.09ms, 10.3MB)
테스트 2 〉	통과 (0.05ms, 10.4MB)
테스트 3 〉	통과 (0.06ms, 10.1MB)
테스트 4 〉	통과 (2.89ms, 11MB)
테스트 5 〉	통과 (3.19ms, 10.8MB)
테스트 6 〉	통과 (11.59ms, 12.8MB)
테스트 7 〉	통과 (4.45ms, 11.4MB)
테스트 8 〉	통과 (7.04ms, 11.6MB)
테스트 9 〉	통과 (14.20ms, 14MB)
테스트 10 〉통과 (65.78ms, 23.3MB)
효율성  테스트
테스트 1 〉	통과 (394.08ms, 112MB)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	통과 (515.92ms, 118MB)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	실패 (시간 초과)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (시간 초과)
테스트 9 〉	실패 (시간 초과)
테스트 10 〉	통과 (9329.68ms, 1GB)
테스트 11 〉	통과 (9852.38ms, 1.11GB)
테스트 12 〉	실패 (시간 초과)
테스트 13 〉	실패 (시간 초과)
테스트 14 〉	실패 (시간 초과)
테스트 15 〉	실패 (시간 초과)
테스트 16 〉	실패 (시간 초과)
테스트 17 〉	실패 (시간 초과)
테스트 18 〉	실패 (시간 초과)
테스트 19 〉	실패 (시간 초과)
테스트 20 〉	실패 (시간 초과)
테스트 21 〉	실패 (시간 초과)
테스트 22 〉	
테스트 23 〉	실패 (시간 초과)
테스트 24 〉	
테스트 25 〉	
테스트 26 〉	
테스트 27 〉	
테스트 28 〉	
테스트 29 〉	
테스트 30 〉	
'''