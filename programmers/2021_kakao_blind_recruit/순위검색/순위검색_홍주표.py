from collections import defaultdict

def solution_failed_1(info, query):
    language = defaultdict(set)
    position = defaultdict(set)
    level = defaultdict(set)
    soul_food = defaultdict(set)
    scores = defaultdict(set)
    
    for idx, string in enumerate(info):
        lang, pos, lev, food, score = string.split()
        language[lang].add(idx)
        position[pos].add(idx)
        level[lev].add(idx)
        soul_food[food].add(idx)
        scores[int(score)].add(idx)
    
    result = []
    
    for q in query:
        lang, _, pos, _, lev, _, food, score = q.split()
        candidates = set()
        for key in scores.keys():
            if key >= int(score):
                candidates |= scores[key]
        if lang != '-':
            candidates &= language[lang]
        if pos != '-':
            candidates &= position[pos]
        if lev != '-':
            candidates &= level[lev]
        if food != '-':
            candidates &= soul_food[food]
        # print(candidates)
        result.append(len(candidates))
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.14ms, 10.3MB)
테스트 2 〉	통과 (0.14ms, 10.2MB)
테스트 3 〉	통과 (0.96ms, 10.4MB)
테스트 4 〉	통과 (5.72ms, 10.5MB)
테스트 5 〉	통과 (15.09ms, 10.4MB)
테스트 6 〉	통과 (18.13ms, 10.5MB)
테스트 7 〉	통과 (18.22ms, 10.4MB)
테스트 8 〉	통과 (29.26ms, 12.5MB)
테스트 9 〉	통과 (45.83ms, 13MB)
테스트 10 〉	통과 (89.31ms, 13.5MB)
테스트 11 〉	통과 (21.75ms, 10.3MB)
테스트 12 〉	통과 (48.82ms, 10.6MB)
테스트 13 〉	통과 (20.92ms, 10.5MB)
테스트 14 〉	통과 (98.48ms, 12MB)
테스트 15 〉	통과 (89.55ms, 12.1MB)
테스트 16 〉	통과 (13.91ms, 10.4MB)
테스트 17 〉	통과 (49.32ms, 10.5MB)
테스트 18 〉	통과 (88.95ms, 11.9MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)

채점 결과
정확성: 40.0
효율성: 0.0
"""

from collections import defaultdict

def solution_failed_2(info, query):
    candidates = defaultdict(list)
    
    for string in info:
        language, position, level, soul_food, score = string.split()
        for lang in (language, '-'):
            for pos in (position, '-'):
                for lv in (level, '-'):
                    for food in (soul_food, '-'):
                        candidates[''.join((lang, pos, lv, food))].append(int(score))
    result = []

    for q in query:
        lang, _, pos, _, lv, _, food, score = q.split()
        scores = sorted(candidates[''.join((lang, pos, lv, food))])
        left, right, mid, score = 0, len(scores) - 1, 0, int(score)
        while left <= right:
            mid = (left + right) // 2
            if scores[mid] >= score:
                right = mid - 1
            else:
                left = mid + 1
        result.append(len(scores) - left)
    return result


"""
정확성  테스트
테스트 1 〉	통과 (0.30ms, 10.4MB)
테스트 2 〉	통과 (0.31ms, 10.4MB)
테스트 3 〉	통과 (0.50ms, 10.4MB)
테스트 4 〉	통과 (1.69ms, 10.4MB)
테스트 5 〉	통과 (3.18ms, 10.5MB)
테스트 6 〉	통과 (6.90ms, 10.5MB)
테스트 7 〉	통과 (3.89ms, 10.8MB)
테스트 8 〉	통과 (39.13ms, 11.5MB)
테스트 9 〉	통과 (44.69ms, 13.2MB)
테스트 10 〉	통과 (41.74ms, 13.7MB)
테스트 11 〉	통과 (3.22ms, 10.5MB)
테스트 12 〉	통과 (6.98ms, 10.6MB)
테스트 13 〉	통과 (3.96ms, 10.7MB)
테스트 14 〉	통과 (26.30ms, 12.2MB)
테스트 15 〉	통과 (26.46ms, 12.2MB)
테스트 16 〉	통과 (2.95ms, 10.5MB)
테스트 17 〉	통과 (7.04ms, 10.6MB)
테스트 18 〉	통과 (23.29ms, 12.1MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
채점 결과
정확성: 40.0
효율성: 0.0
합계: 40.0 / 100.0
"""


from collections import defaultdict

def solution(info, query):
    candidates = defaultdict(list)
    
    for string in info:
        language, position, level, soul_food, score = string.split()
        for lang in (language, '-'):
            for pos in (position, '-'):
                for lv in (level, '-'):
                    for food in (soul_food, '-'):
                        candidates[''.join((lang, pos, lv, food))].append(int(score))
    
    for key in candidates.keys():
        candidates[key].sort()

    result = []

    for q in query:
        lang, _, pos, _, lv, _, food, score = q.split()
        scores = candidates[''.join((lang, pos, lv, food))]
        left, right, mid, score = 0, len(scores) - 1, 0, int(score)
        while left <= right:
            mid = (left + right) // 2
            if scores[mid] >= score:
                right = mid - 1
            else:
                left = mid + 1
        result.append(len(scores) - left)
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.33ms, 10.5MB)
테스트 2 〉	통과 (0.33ms, 10.4MB)
테스트 3 〉	통과 (0.51ms, 10.4MB)
테스트 4 〉	통과 (1.55ms, 10.5MB)
테스트 5 〉	통과 (2.49ms, 10.6MB)
테스트 6 〉	통과 (5.31ms, 10.5MB)
테스트 7 〉	통과 (3.23ms, 10.6MB)
테스트 8 〉	통과 (41.77ms, 11.3MB)
테스트 9 〉	통과 (43.69ms, 13.3MB)
테스트 10 〉	통과 (41.94ms, 13.7MB)
테스트 11 〉	통과 (2.70ms, 10.4MB)
테스트 12 〉	통과 (5.05ms, 10.7MB)
테스트 13 〉	통과 (3.22ms, 10.8MB)
테스트 14 〉	통과 (22.77ms, 12.1MB)
테스트 15 〉	통과 (22.64ms, 12.1MB)
테스트 16 〉	통과 (2.38ms, 10.5MB)
테스트 17 〉	통과 (4.93ms, 10.7MB)
테스트 18 〉	통과 (21.60ms, 12.1MB)
효율성  테스트
테스트 1 〉	통과 (804.42ms, 63.5MB)
테스트 2 〉	통과 (892.72ms, 63.6MB)
테스트 3 〉	통과 (776.16ms, 63.3MB)
테스트 4 〉	통과 (900.54ms, 63.9MB)
채점 결과
정확성: 40.0
효율성: 60.0
합계: 100.0 / 100.0
"""
