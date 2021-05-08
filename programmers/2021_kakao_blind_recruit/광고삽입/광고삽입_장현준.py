'''
00:00:00 ~ 99:59:59 : 36만
logs : 30만 * 2 = 60만

'''
from datetime import datetime

def str_to_sec(str):
    return int(str[0:2]) * 3600 + int(str[3:5]) * 60 + int(str[6:8])

def sec_to_str(sec):
    return f'{sec//3600:02}:{sec%3600//60:02}:{sec%60:02}'

def solution(play_time, adv_time, logs):
    
    t = [0] * 360000 # 00:00:00 ~ 99:59:59
    
    N = str_to_sec(adv_time)

    last = 0
    for log in logs:
        st, end = map(str_to_sec, log.split("-"))
        t[st] += 1
        t[end] -= 1
        last = max(last, end)
    
    cnt = 0
    for i in range(360000):
        cnt += t[i]
        t[i] = cnt
        
    max_val = now = sum(t[:N])
    max_idx = 0

    if last <= N:
        return sec_to_str(max_idx)

    for i in range(last-N+1):
        now += t[i+N] - t[i]
        if now > max_val:
            max_val, max_idx = now, i+1
    return sec_to_str(max_idx)
'''
정확성  테스트
테스트 1 〉	통과 (27.25ms, 12.7MB)
테스트 2 〉	통과 (35.47ms, 13.3MB)
테스트 3 〉	통과 (41.99ms, 13.9MB)
테스트 4 〉	통과 (165.41ms, 27.7MB)
테스트 5 〉	통과 (236.75ms, 21.2MB)
테스트 6 〉	통과 (67.80ms, 12.7MB)
테스트 7 〉	통과 (414.90ms, 42.8MB)
테스트 8 〉	통과 (410.59ms, 42.5MB)
테스트 9 〉	통과 (586.02ms, 52.3MB)
테스트 10 〉통과 (688.64ms, 49.9MB)
테스트 11 〉통과 (592.34ms, 49.9MB)
테스트 12 〉통과 (580.72ms, 40.8MB)
테스트 13 〉통과 (598.83ms, 49.6MB)
테스트 14 〉통과 (570.10ms, 40.8MB)
테스트 15 〉통과 (41.64ms, 12.7MB)
테스트 16 〉통과 (567.97ms, 40.6MB)
테스트 17 〉통과 (632.94ms, 50.4MB)
테스트 18 〉통과 (577.98ms, 40.7MB)
테스트 19 〉통과 (26.32ms, 12.6MB)
테스트 20 〉통과 (25.73ms, 12.8MB)
테스트 21 〉통과 (181.63ms, 21.3MB)
테스트 22 〉통과 (193.14ms, 21.2MB)
테스트 23 〉통과 (623.65ms, 45.7MB)
테스트 24 〉통과 (561.27ms, 40.8MB)
테스트 25 〉통과 (56.10ms, 12.6MB)
테스트 26 〉통과 (34.01ms, 13MB)
테스트 27 〉통과 (31.07ms, 13.6MB)
테스트 28 〉통과 (50.44ms, 14.1MB)
테스트 29 〉통과 (34.02ms, 14.2MB)
테스트 30 〉통과 (26.51ms, 13.8MB)
테스트 31 〉통과 (26.67ms, 13.6MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''