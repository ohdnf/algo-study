# stones 1 ~ 200,000 => 매번 순회하여 (if + 할당 + if) => 600,000
# stones 원소 값 : 1 ~ 200,000,000 => 이분탐색 => 2 ** 28
# 18,000,000
# 카카오에 따르면 (O(len(stones) log max(stones)))
def solution(stones, jump):
    # 1. n-1건넜다고 가정 n은 가능?
    def check(mid):
        cnt = 0
        for stone in stones:
            if stone - mid < 0:
                cnt += 1
            else:
                cnt = 0
            if cnt == jump:
                return False # 유효범위 lt ~ mid-1
        return True # 유효범위 mid ~ rt
    lt = 0
    rt = max(stones)

    while lt != rt:
        mid = (lt+rt+1)//2
        if check(mid):
            # 2-1. 가능 => mid보다 큰 영역에서 검색 (lt == mid에선 이미 가능)
            lt = mid
        else:
            # 2-2. 불가능 => mid보다 작은 영역에서 검색
            rt = mid-1
    return lt
    # lt: 가능함, rt: 가능할수있는 최대 영역!!!
    # lt == rt => 정답!

    # 위아래는 소요 시간은 거의 동일
    # lt: lt-1은 가능!, rt: 가능할수 있는 최대 영역!!!
    # lt-1 == rt <=> lt > rt => 정답은 lt!
    lt = 1
    rt = max(stones)

    while lt <= rt:
        mid = (lt+rt)//2
        if check(mid):
            # 2-1. 가능 => mid보다 큰 영역에서 검색
            lt = mid + 1
        else:
            # 2-2. 불가능 => mid보다 작은 영역에서 검색
            rt = mid - 1
    return lt-1
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.03ms, 10.2MB)
# 테스트 5 〉	통과 (0.03ms, 10.2MB)
# 테스트 6 〉	통과 (0.37ms, 10.2MB)
# 테스트 7 〉	통과 (1.02ms, 10.2MB)
# 테스트 8 〉	통과 (0.61ms, 10.3MB)
# 테스트 9 〉	통과 (1.05ms, 10.2MB)
# 테스트 10 〉	통과 (0.03ms, 10.3MB)
# 테스트 11 〉	통과 (0.02ms, 10.2MB)
# 테스트 12 〉	통과 (0.03ms, 10.2MB)
# 테스트 13 〉	통과 (0.06ms, 10.2MB)
# 테스트 14 〉	통과 (0.33ms, 10.2MB)
# 테스트 15 〉	통과 (1.12ms, 10.2MB)
# 테스트 16 〉	통과 (0.85ms, 10.2MB)
# 테스트 17 〉	통과 (1.00ms, 10.2MB)
# 테스트 18 〉	통과 (0.02ms, 10.2MB)
# 테스트 19 〉	통과 (0.04ms, 10.2MB)
# 테스트 20 〉	통과 (0.08ms, 10.2MB)
# 테스트 21 〉	통과 (0.45ms, 10.2MB)
# 테스트 22 〉	통과 (1.07ms, 10.3MB)
# 테스트 23 〉	통과 (0.75ms, 10.2MB)
# 테스트 24 〉	통과 (1.04ms, 10.2MB)
# 테스트 25 〉	통과 (0.01ms, 10.1MB)
# 효율성  테스트
# 테스트 1 〉	통과 (279.61ms, 18.5MB)
# 테스트 2 〉	통과 (327.64ms, 18.7MB)
# 테스트 3 〉	통과 (358.17ms, 18.7MB)
# 테스트 4 〉	통과 (217.03ms, 18.6MB)
# 테스트 5 〉	통과 (235.12ms, 18.7MB)
# 테스트 6 〉	통과 (255.60ms, 18.7MB)
# 테스트 7 〉	통과 (379.78ms, 18.6MB)
# 테스트 8 〉	통과 (402.61ms, 18.6MB)
# 테스트 9 〉	통과 (391.71ms, 18.6MB)
# 테스트 10 〉	통과 (394.45ms, 18.5MB)
# 테스트 11 〉	통과 (365.65ms, 18.6MB)
# 테스트 12 〉	통과 (390.33ms, 18.7MB)
# 테스트 13 〉	통과 (254.35ms, 18.7MB)
# 테스트 14 〉	통과 (207.57ms, 18.6MB)

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