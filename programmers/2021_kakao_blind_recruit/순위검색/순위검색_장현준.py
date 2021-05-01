from collections import defaultdict
def create_key(a,b,c,d):
    lst = []
    for k1 in (a, '-'):
        for k2 in (b, '-'):
            for k3 in (c, '-'):
                for k4 in (d, '-'):
                    lst.append( (k1,k2,k3,k4) )
    return lst

def binary_search(lst, e):
    if len(lst) == 0 or lst[-1] < e: # 빈 리스트 or 가장 큰 값도 만족하지 못함
        return 0
    if lst[0] >= e: # 가장 작은 값도 만족
        return len(lst)
    
    start = 0
    end = len(lst)-1
    
    while start <= end:
        mid = (start+end) // 2
        if lst[mid] < e:
            start = mid + 1
        else:
            end = mid - 1
    return (len(lst)-1) - end

def solution(infos, queries):
    # info로 table 데이터 생성
    table = defaultdict(list)
    for info in infos:
        a, b, c, d, e = info.split()
        e = int(e)
        for key in create_key(a,b,c,d):
            table[key].append(e)
        
    for k, v in table.items():
        v.sort()
        # print(f'k:{k}, v:{v}')
    
    answer = []
    # query로 result 원소 생성
    for query in queries:
        a, b, c, d = query.split(" and ")
        d, e = d.split()
        e = int(e)
        if (a,b,c,d) in table:
            answer.append(binary_search(table[(a,b,c,d)],e))
        else:
            answer.append(0)
        
    return answer
'''
정확성  테스트
테스트 1 〉	통과 (0.26ms, 10.5MB)
테스트 2 〉	통과 (0.27ms, 10.4MB)
테스트 3 〉	통과 (0.47ms, 10.5MB)
테스트 4 〉	통과 (1.59ms, 10.5MB)
테스트 5 〉	통과 (2.81ms, 10.5MB)
테스트 6 〉	통과 (4.63ms, 10.4MB)
테스트 7 〉	통과 (3.49ms, 10.8MB)
테스트 8 〉	통과 (29.41ms, 11.4MB)
테스트 9 〉	통과 (30.09ms, 11.5MB)
테스트 10 〉통과 (33.29ms, 11.6MB)
테스트 11 〉통과 (2.44ms, 10.6MB)
테스트 12 〉통과 (4.32ms, 10.5MB)
테스트 13 〉통과 (3.11ms, 10.8MB)
테스트 14 〉통과 (16.46ms, 10.9MB)
테스트 15 〉통과 (15.72ms, 11MB)
테스트 16 〉통과 (2.75ms, 10.6MB)
테스트 17 〉통과 (4.79ms, 10.5MB)
테스트 18 〉통과 (16.66ms, 11MB)
효율성  테스트
테스트 1 〉	통과 (616.90ms, 42.6MB)
테스트 2 〉	통과 (659.92ms, 42.8MB)
테스트 3 〉	통과 (670.10ms, 42.4MB)
테스트 4 〉	통과 (671.81ms, 42.6MB)
'''