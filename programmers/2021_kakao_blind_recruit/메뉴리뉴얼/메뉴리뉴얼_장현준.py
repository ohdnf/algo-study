'''
제한조건
코스요리
- 2가지 이상의 단품메뉴 구성
- 2명 이상의 손님으로부터 주문된 단품 조합

주문
- 명수: 2 ~20
- 각 주문: 2 ~ 10

코스
- 갯수: 1 ~ 10
- 각 원소: 2 ~ 10, 오름차순
'''
from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    # 가능한 조합
    available = defaultdict(int)
    for order in orders:
        for n in range(2, len(order)+1):
            for combi in combinations(sorted(order), n):
                available["".join(combi)] += 1
    # course 별 메뉴 선정
    answer = {k: [0, []] for k in course}
    for key, cnt in available.items():
        if len(key) not in answer or cnt < 2:
            continue
        if cnt > answer[len(key)][0]:
            answer[len(key)] = [cnt, [key]]
        elif cnt == answer[len(key)][0]:
            answer[len(key)][1].append(key)
    # 선정된 메뉴 정렬해서 리턴
    return sorted([v for _, lst in answer.values() for v in lst])
'''
테스트 1 〉	통과 (0.22ms, 10.3MB)
테스트 2 〉	통과 (0.11ms, 10.1MB)
테스트 3 〉	통과 (0.23ms, 10.2MB)
테스트 4 〉	통과 (0.20ms, 10.3MB)
테스트 5 〉	통과 (0.18ms, 10.2MB)
테스트 6 〉	통과 (0.55ms, 10.3MB)
테스트 7 〉	통과 (0.54ms, 10.3MB)
테스트 8 〉	통과 (6.10ms, 10.5MB)
테스트 9 〉	통과 (3.91ms, 10.5MB)
테스트 10 〉	통과 (5.36ms, 10.8MB)
테스트 11 〉	통과 (3.76ms, 10.5MB)
테스트 12 〉	통과 (3.21ms, 10.5MB)
테스트 13 〉	통과 (5.78ms, 10.9MB)
테스트 14 〉	통과 (6.76ms, 10.7MB)
테스트 15 〉	통과 (5.48ms, 10.9MB)
테스트 16 〉	통과 (6.14ms, 10.6MB)
테스트 17 〉	통과 (8.13ms, 10.8MB)
테스트 18 〉	통과 (9.86ms, 10.8MB)
테스트 19 〉	통과 (8.39ms, 10.6MB)
테스트 20 〉	통과 (7.46ms, 10.5MB)
'''