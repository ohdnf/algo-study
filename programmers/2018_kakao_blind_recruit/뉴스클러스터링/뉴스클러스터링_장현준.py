def solution(str1, str2):
    '''
    35분 소요
    자카드 유사도
    J(A, B)
        교집합크기 / 합집합크기 or 1(둘다 공집합일때)
    다중집합
        원소의 중복 허용
    자카드 유사도 다중집합 적용
        교집합 min / 합집합 max
    65536 곱하여 활용
    '''
    # chd: 숫자 => 글자
    # ord: 글자 => 숫자
    s1 = dict()
    s2 = dict()
    for i in range(len(str1)-1):
        # 문제 조건대로 2글자씩 끊어서 진행
        ch = str1[i : i+2].lower() # 대문자 => 소문자로 일괄 변환
        if ('a' <= ch[0] <= 'z') and ('a' <= ch[1] <= 'z'): # 영문자쌍만 유효
            if ch in s1:
                s1[ch] += 1
            else:
                s1[ch] = 1

    for i in range(len(str2)-1):
        ch = str2[i : i+2].lower()
        if ('a' <= ch[0] <= 'z') and ('a' <= ch[1] <= 'z'):
            if ch in s2:
                s2[ch] += 1
            else:
                s2[ch] = 1
    inter = 0
    union = 0
    for ch in s1.keys():
        if ch in s2:
            # 공통 요소
            inter += min(s1[ch], s2[ch])
            union += max(s1[ch], s2[ch])
        else:
            # 공통 요소 아님
            union += s1[ch]
            
    for ch in s2.keys():
        # 공통 요소는 위에서 체크했으므로 확인 할 필요 없음
        if ch not in s1:
            # 공통 요소 아님
            union += s2[ch]
    if union:
        # 65536 * J(A, B)
        return 65536 * inter // union
    else:
        # 문제 조건 => 나눗셈이 정의 되지 않을떄 => J(A, B)는 1
        return 65536
'''
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.4MB)
테스트 4 〉	통과 (1.34ms, 10.3MB)
테스트 5 〉	통과 (0.04ms, 10.4MB)
테스트 6 〉	통과 (1.02ms, 10.2MB)
테스트 7 〉	통과 (0.11ms, 10.5MB)
테스트 8 〉	통과 (0.03ms, 10.3MB)
테스트 9 〉	통과 (0.10ms, 10.3MB)
테스트 10 〉통과 (0.19ms, 10.2MB)
테스트 11 〉통과 (0.33ms, 10.3MB)
테스트 12 〉통과 (0.01ms, 10.3MB)
테스트 13 〉통과 (0.06ms, 10.4MB)
'''