from collections import defaultdict, Counter
from itertools import combinations

def solution(orders, course):
    menus = Counter()
    for order in orders:
        for length in range(2, len(order) + 1):
            for combi in combinations(order, length):
                menus[''.join(sorted(combi))] += 1
    order_count = defaultdict(list)
    for menu, count in menus.items():
        if len(menu) in course:
            order_count[len(menu)].append((menu, count))
    result = []
    for count, courses in order_count.items():
        courses.sort(key=lambda c: (-c[1], c[0]))
        max_order_count = courses[0][1]
        for course, count in courses:
            if count == max_order_count and count > 1:
                result.append(course)
    return sorted(result)


"""
정확성  테스트
테스트 1 〉	통과 (0.30ms, 10.1MB)
테스트 2 〉	통과 (0.17ms, 10.2MB)
테스트 3 〉	통과 (0.29ms, 10.3MB)
테스트 4 〉	통과 (0.26ms, 10.3MB)
테스트 5 〉	통과 (0.24ms, 10.3MB)
테스트 6 〉	통과 (0.74ms, 10.3MB)
테스트 7 〉	통과 (0.66ms, 10.1MB)
테스트 8 〉	통과 (6.02ms, 10.4MB)
테스트 9 〉	통과 (4.88ms, 10.4MB)
테스트 10 〉	통과 (8.90ms, 11.1MB)
테스트 11 〉	통과 (5.49ms, 10.6MB)
테스트 12 〉	통과 (5.51ms, 10.7MB)
테스트 13 〉	통과 (8.82ms, 11MB)
테스트 14 〉	통과 (8.61ms, 11MB)
테스트 15 〉	통과 (7.66ms, 10.9MB)
테스트 16 〉	통과 (6.50ms, 10.6MB)
테스트 17 〉	통과 (9.35ms, 10.8MB)
테스트 18 〉	통과 (13.23ms, 10.9MB)
테스트 19 〉	통과 (15.99ms, 10.6MB)
테스트 20 〉	통과 (8.96ms, 10.5MB)
"""
