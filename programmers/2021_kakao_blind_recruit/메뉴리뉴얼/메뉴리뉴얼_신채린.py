from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    # course 개수마다 파악 
    for num in course:
        available = []
        # 각 order별로 가능한 조합 추가 
        for order in orders:
            combi = combinations(sorted(order), num)
            available.extend(tuple(combi))
        # 해당 조합들의 빈도수 체크 
        counter = Counter(available)
        # 빈도수가 높은 순으로 정렬
        most = Counter.most_common(counter)
        for menu, cnt in most:
            # 최소 2명 이상의 손님부터 포함 
            if cnt > 1 and cnt == most[0][1]:
                answer.append(''.join(menu))

    return sorted(answer)