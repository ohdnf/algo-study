'''2019 카카오 블라인드 3번째 문제
후보키
- Relation의 tuple을 유일하게 식별할 수 있는 속성  attr or 속성의 집합 중에서
    - uniqueness: Relation의 모든 tuple에 대해 유일하게 식별되어야한다.
    - minimality: 유일성 키를 구성하는 attr중 하나라도 제외하는 경우 유일성이 깨지는 경우

예시
- 학번
- 이름 & 전공

입력
- relation
    - column: 1~8
    - row: 1~20
    - 문자열 구성: 소문자 or 숫자
'''
from itertools import combinations

def solution(relation):
    num_of_col = len(relation[0])
    num_of_row = len(relation)
    
    answer = []
    
    for n in range(1, num_of_col+1):
        for lst in combinations(list(range(num_of_col)), n): # 가능한 col 선택 조합
            # 1. 최소성 확인
            poss = True
            for i in range(1, len(lst)+1):
                for e in answer:
                    if e.issubset(set(lst[:i])):
                        poss = False
                        break
            if not poss:
                continue
            # answer.append(set(lst)) # 최소성 확인 나중에 할때

            # 2. 후보 키 가능여부 확인
            d = dict()
            poss2 = True
            for r in range(num_of_row):
                key = str([relation[r][c] for c in lst])
                if key in d:
                    poss2 = False
                    break
                d[key] = 1
            if not poss2:
                continue
            else: # 후보 키 가능여부 확인 나중에 할때
                answer.append(set(lst))
    return len(answer)

# 속도 >>>  최소성 확인 먼저 > 후보키 가능성 확인 먼저
'''
1. 최소성 확인 먼저
테스트 1 〉	통과 (0.07ms, 10.2MB)
테스트 2 〉	통과 (0.08ms, 10.3MB)
테스트 3 〉	통과 (0.09ms, 10.2MB)
테스트 4 〉	통과 (0.10ms, 10.3MB)
테스트 5 〉	통과 (0.11ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.03ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.3MB)
테스트 9 〉	통과 (0.18ms, 10.2MB)
테스트 10 〉통과 (0.11ms, 10.4MB)
테스트 11 〉통과 (0.29ms, 10.3MB)
테스트 12 〉통과 (1.08ms, 10.3MB)
테스트 13 〉통과 (0.63ms, 10.2MB)
테스트 14 〉통과 (0.07ms, 10.2MB)
테스트 15 〉통과 (0.07ms, 10.1MB)
테스트 16 〉통과 (0.09ms, 10.2MB)
테스트 17 〉통과 (0.09ms, 10.2MB)
테스트 18 〉통과 (2.31ms, 10.3MB)
테스트 19 〉통과 (1.76ms, 10.4MB)
테스트 20 〉통과 (2.43ms, 10.2MB)
테스트 21 〉통과 (1.88ms, 10.3MB)
테스트 22 〉통과 (2.66ms, 10.3MB)
테스트 23 〉통과 (0.12ms, 10.2MB)
테스트 24 〉통과 (2.95ms, 10.2MB)
테스트 25 〉통과 (2.10ms, 10.3MB)
테스트 26 〉통과 (1.46ms, 10.2MB)
테스트 27 〉통과 (0.41ms, 10.3MB)
테스트 28 〉통과 (0.63ms, 10.3MB)
'''

'''
2. 후보키 확인 먼저
테스트 1 〉	통과 (0.11ms, 10.2MB)
테스트 2 〉	통과 (0.12ms, 10.2MB)
테스트 3 〉	통과 (0.11ms, 10.3MB)
테스트 4 〉	통과 (0.11ms, 10.3MB)
테스트 5 〉	통과 (0.08ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.03ms, 10.2MB)
테스트 8 〉	통과 (0.03ms, 10.2MB)
테스트 9 〉	통과 (0.25ms, 10.3MB)
테스트 10 〉통과 (0.38ms, 10.3MB)
테스트 11 〉통과 (0.54ms, 10.3MB)
테스트 12 〉통과 (2.01ms, 10.3MB)
테스트 13 〉통과 (1.07ms, 10.3MB)
테스트 14 〉통과 (0.10ms, 10.3MB)
테스트 15 〉통과 (0.12ms, 10.2MB)
테스트 16 〉통과 (0.14ms, 10.4MB)
테스트 17 〉통과 (0.13ms, 10.3MB)
테스트 18 〉통과 (7.27ms, 10.2MB)
테스트 19 〉통과 (3.21ms, 10.2MB)
테스트 20 〉통과 (6.66ms, 10.2MB)
테스트 21 〉통과 (1.56ms, 10.3MB)
테스트 22 〉통과 (2.27ms, 10.1MB)
테스트 23 〉통과 (0.16ms, 10.3MB)
테스트 24 〉통과 (3.62ms, 10.3MB)
테스트 25 〉통과 (5.98ms, 10.3MB)
테스트 26 〉통과 (3.00ms, 10.3MB)
테스트 27 〉통과 (0.98ms, 10.3MB)
테스트 28 〉통과 (0.83ms, 10.4MB)
'''


