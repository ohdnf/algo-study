# 자카드 유사도 J (A, B) - 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값으로 정의된다.
# 공집합일때는 1로 정의한다.
# 원소의 중복을 허용하는 다중집합에 대해 확장할 수 있다.
# 입력: 영문자로 된 글자쌍만 유효하고, 기타 공백이나 숫자, 특수 문자가 있으면 그 글자 쌍은 버리기
# 출력형식 - 65536을 곱한 후 소수점 아래를 버리고 정수부만 출력

import math 
def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    list1 = []
    list2 = []
    
    # 2글자씩 끊어서 다중집합 원소 만들기
    for i in range(0, len(str1)-1):
        word = str1[i:i+2]
        if 'A' <= word[0] <= 'Z' and 'A' <= word[1] <= 'Z':
            list1.append(word)
    
    for i in range(0, len(str2)-1):
        word = str2[i:i+2]
        
        if 'A' <= word[0] <= 'Z' and 'A' <= word[1] <= 'Z':
            list2.append(word)
    
    # 전체 길이 
    cnt = len(list1) + len(list2)

    # 둘다 공집합이면 65536 리턴
    if cnt == 0:
        return 65536
    
    # 교집합 원소 개수 
    cntInter = 0

    for idx1, value1 in enumerate(list1):
        for idx2, value2 in enumerate(list2):
            if value1 == value2:
                # 이미 중복된 패턴이므로 -1로 바꾸기 
                list2[idx2] = "-1"
                cntInter += 1
                break 
    return math.floor(cntInter/(cnt-cntInter)*65536)
