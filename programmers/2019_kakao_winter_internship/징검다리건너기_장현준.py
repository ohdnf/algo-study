# 옛날 도전하던 로직 => 실패함
def solution(stones, jump):
    # 1:56
    # 1.디딤돌
        # 숫자 딛을때마다 -1
        # 0은 딛을 수 없다.
    # 2. 무조건 !!! 가까운 디딤돌부터 딛는다. => 시뮬레이션
    # 3. 한 명씩 건넌다.
    # 4. 친구들은 무한.
    
    # 5. stones 1 ~ 200,000 => 2십만 정돈 단순 순회는 okay
    # 6. stones 원소 값 : 1 ~ 200,000,000
    # 즉, 그냥 풀 생각은 마라 ㅡㅅㅡ
    
    ########## 로직 구현 ###########

    # answer = 0
    # 1-1. dict로 옮겨보자. values = 디딤돌값 : [리스트], removed : 사라진 디딤돌 리스트
    values = dict()
    removed = []
    for idx, val in enumerate(stones):
        # 1-2. 해당 디딤돌값이 있다면 append => values[디딤돌값].append(디딤돌인덱스)
        if val in values:
            values[val].append(idx)
        # 1-3. 없다면 생성 => values[디딤돌값] = [디딤돌인덱스]
        else:
            values[val] = [idx]
    # 여기까지 2:09, 13분 경과
    
    k = 0
    # return 0 not in values
    while True:
        # 2-1. 이전 단계에 없어진 디딤돌이 없다면, 무조건 통과
        if k not in values:
            k += 1
            continue
        # 2-2. 이전 단계에 사라진 디딤돌이 있다
        
        # 3-1. 이전 단계에서 사라진 디딤돌을 저장
        for n in values[k]:
            removed.append(n)
            
            # 3-2. 사라진 디딤돌 리스트 removed를 sort
            removed.sort()
        
        # 4. 업데이트된 removed를 토대로 통과 할 수 있는지 검사
        
        # 4-1. removed를 순회하여 최장거리 탐색
        longest = 1
        for i in range(1, len(removed)):
            if removed[i-1] + 1 == removed[i]:
                longest += 1
                # 4-2. jump와 비교 => jump == 최장거리 => 게임 종료 조건
                if jump <= longest:
                    return k
            else:
                longest = 1
        
        # 4-3. 통과 => 계속
        # answer += 1
        k += 1
        # 로직 한번 구현 끝 2:42, 48분 경과 => 구현 오류
        # 두번째 로직 구현 끝 2:52, 58분 경과

    # 로직 글로 구현 2:18, 22분 경과