def solution(str1, str2):
    '''
    1. 각 문자를 길이 2의 글자쌍의 집합으로 만들기
        - 영문자로 된 글자쌍만 남기기
        - 소문자화 하기
    2. 두 집합의 교집합과 합집합의 크기 구하기
    3. int(자카드 유사도 * 65536) 출력
    '''
    answer = 65536 # 자카드 유사도가 1인 경우
    
    import re
    p = re.compile('[a-zA-Z][a-zA-Z]')
            
    def f(string): # 소문자 영문자 검증한 문자열 글자쌍의 배열을 리턴
        str_set = []
        for i in range(len(string)-1):
            tmp_str = string[i:i+2]
            if p.match(tmp_str):
                str_set.append(tmp_str.lower())
        return str_set
            
    str_set1 = f(str1)
    str_set2 = f(str2)
    visited = [0]*len(str_set2) # 이미 매칭되었는 지 확인
    count = 0 # 서로 겹치는 글자쌍의 개수
    
    for i in range(len(str_set1)):
        for j in range(len(str_set2)):
            if not visited[j] and str_set1[i] == str_set2[j]:
                count += 1
                visited[j] = 1
                break
                
    if len(str_set1) + len(str_set2) - count: # 아닌 경우, 자카드 유사도는 1
        answer = int((count / (len(str_set1) + len(str_set2) - count))*65536)
    
    return answer

'''
26분 소요

정확성 테스트
테스트 1 〉	통과 (0.14ms, 10.3MB)
테스트 2 〉	통과 (0.15ms, 10.2MB)
테스트 3 〉	통과 (0.12ms, 10.2MB)
테스트 4 〉	통과 (8.58ms, 10.3MB)
테스트 5 〉	통과 (0.15ms, 10.3MB)
테스트 6 〉	통과 (0.14ms, 10.1MB)
테스트 7 〉	통과 (0.42ms, 10.3MB)
테스트 8 〉	통과 (0.14ms, 10.2MB)
테스트 9 〉	통과 (0.35ms, 10.3MB)
테스트 10 〉	통과 (0.92ms, 10.2MB)
테스트 11 〉	통과 (1.17ms, 10.2MB)
테스트 12 〉	통과 (0.13ms, 10.2MB)
테스트 13 〉	통과 (0.27ms, 10.4MB)
'''