# 효율성 통과 코드
# 기존 코드 (아래 코드)에 combinations로 대체 + 미리 counting 딕셔너리의 sorting 진행 

from collections import defaultdict
from itertools import combinations
def solution(info, query):
    answer = []
    counting = defaultdict(list)
    for i in info:
        # 각 정보 split 진행하기 
        splitted = i.split() 
        key = splitted[:-1]
        val = int(splitted[-1])
        
        combis = []
        
        
        # 16가지 경우를 모두 사전에 key로 등록 (value는 점수 넣기 )
        for k in range(5):
            # 16가지 경우의 수를 만들기
            for c in combinations(key, k):
                temp = ''.join(c)
                counting[temp].append(val)
    # sorting 진행 
    for key in counting.keys():
        counting[key].sort()
    
    # query를 돌면서 파악 
    for q in query:
        # 각 query split
        q_splitted = q.split(' and ')
        last = q_splitted.pop() 
        q_splitted.extend(last.split())
        
        while '-' in q_splitted:
            q_splitted.remove('-')
        
        # counting 딕셔너리에 활용할 key값 구하기
        q_key = q_splitted[:-1]
        q_value =  int(q_splitted[-1])
        
        numbers = counting[''.join(q_key)]
        
        # 이분탐색하기 
        left, right = 0, len(numbers)
        while left < right:
            mid = (left + right) // 2
            if numbers[mid] >= q_value:
                right = mid
            else:
                left = mid + 1
        answer.append(len(numbers) - left)

    return answer


# 효율성을 통과하지 못한 코드 (정확성만 100%)
from collections import defaultdict
def solution(info, query):
    answer = []
    counting = defaultdict(list)
    for i in info:
        # 각 정보 split 진행하기 
        splitted = i.split() 
        key = splitted[:-1]
        val = int(splitted[-1])
        
        combis = []
        
        # 16가지 경우의 수를 만들기
        def make_combi(keys, depth, combi):
            if depth == 4:
                combis.append(combi)
                return 
            make_combi(keys, depth+1, combi + [keys[depth]])
            make_combi(keys, depth+1, combi + ['-'])
            
        make_combi(key, 0, [])
        
        # 16가지 경우를 모두 사전에 key로 등록 (value는 점수 넣기 )
        for c in combis:
            temp = ''.join(c)
            counting[temp].append(val)
    
    # query를 돌면서 파악 
    for q in query:
        # 각 query split
        q_splitted = q.split(' and ')
        last = q_splitted.pop().split()
        q_splitted.extend(last)
        
        # counting 딕셔너리에 활용할 key값 구하기 (+ 앞으로 사용할 number인 value도!)
        q_key = q_splitted[:-1]
        q_value = int(q_splitted[-1])
        
        # sorting 진행 
        numbers = sorted(counting[''.join(q_key)])
        
        # 이분탐색하기 
        left, right = 0, len(numbers)
        while left < right:
            mid = (left + right) // 2
            if numbers[mid] >= q_value:
                right = mid
            else:
                left = mid + 1
        answer.append(len(numbers) - left)

    return answer