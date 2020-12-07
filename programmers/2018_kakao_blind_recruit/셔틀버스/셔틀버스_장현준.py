def solution(n, t, m, timetable):
    '''
    1회 9:00
    n회 9:00 + (n-1) * t 분, n*m명 탑승
    '''
    # 1. 시분 => 분으로 교체
    for i in range(len(timetable)):
        timetable[i] = int(timetable[i][0:2]) * 60 + int(timetable[i][3:5])
    timetable.sort()
    # 맨 먼저 1분이라도 빨리 오면 무조건 탄다.
    answer = timetable[0] - 1
    now = 0
    # 2. n회 셔틀 운행
    for i in range(n):
        # 출발시간 9:00 + i * t
        time = 540 + i * t
        # 탑승객 최대 m
        taken = 0
        while taken < m:
            # 해당 시간에 대기줄에 사람이 없음 => 태우는 작업 종료
            if now == len(timetable) or timetable[now] > time: break;
            # 한명씩 태우기
            now += 1
            taken += 1
            
        
        # 이번 회차때 자리가 남는다. == 이번 회차에 와도 탈 수 있다.
        if taken < m:
            # 이번 회차때 모두 태웠다. == 마지막 타임에 와도(현재 time 포함) 무조건 탄다.
            if now == len(timetable):
                answer = 540 + (n-1) * t
                break
            # 이번 회차에 와도 탈 수 있다. == 탈 수 있는 가장 늦은 시간 갱신
            answer = time
        else:
            # 이번 회차때 자리가 꽉 찼다. 타려면 마지막에 탄 놈(now-1)보단 1분이라도 빨라야한다.
            if now-1 >= 0: # now-1이 음수가 되면 에러
                answer = timetable[now-1] - 1
            
    return str(answer // 60).zfill(2) + ":" + str(answer % 60).zfill(2)
'''
테스트 1 〉	통과 (0.03ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (0.04ms, 10.4MB)
테스트 4 〉	통과 (0.03ms, 10.4MB)
테스트 5 〉	통과 (0.05ms, 10.4MB)
테스트 6 〉	통과 (0.04ms, 10.3MB)
테스트 7 〉	통과 (0.56ms, 10.4MB)
테스트 8 〉	통과 (0.03ms, 10.5MB)
테스트 9 〉	통과 (2.48ms, 10.3MB)
테스트 10 〉	통과 (0.03ms, 10.5MB)
테스트 11 〉	통과 (0.05ms, 10.4MB)
테스트 12 〉	통과 (0.32ms, 10.4MB)
테스트 13 〉	통과 (0.43ms, 10.5MB)
테스트 14 〉	통과 (0.07ms, 10.4MB)
테스트 15 〉	통과 (0.10ms, 10.4MB)
테스트 16 〉	통과 (0.20ms, 10.5MB)
테스트 17 〉	통과 (0.48ms, 10.3MB)
테스트 18 〉	통과 (0.43ms, 10.4MB)
테스트 19 〉	통과 (0.46ms, 10.3MB)
테스트 20 〉	통과 (0.43ms, 10.4MB)
테스트 21 〉	통과 (0.45ms, 10.3MB)
테스트 22 〉	통과 (1.43ms, 10.5MB)
테스트 23 〉	통과 (1.44ms, 10.5MB)
테스트 24 〉	통과 (0.56ms, 10.4MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''