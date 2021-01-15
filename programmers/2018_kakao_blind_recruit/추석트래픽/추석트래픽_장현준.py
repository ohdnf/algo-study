def solution(lines):
    '''
    문제
    초당 최대 처리량: 임의시간 기준 1초간 최대 처리량
    
    입력
    lines
    - 길이 N: 1~2000
    - 응답완료시간 S + 처리시간 T
    - S: 고정길이, 2016-09-15 hh:mm:ss.sss
    - T: 초s, 0.001~3.000
    - S 기준 오름차순 정렬
    
    방향성
    # 시간, 출발시간 모두 heapq에 등록 => 하나씩 꺼내 +1 or -1
    '''
    def get_time(line):
        h = int(line[11:13]) * 1000 * 60 * 60
        m = int(line[14:16]) * 1000 * 60
        s1 = int(line[17:19]) * 1000
        s2 = int(line[20:23])
        sec1 = h + m + s1 + s2
        s3 = line[24:len(line)-1].split(".")
        s4 = int(s3[0]) * 1000 if len(s3) == 1 else int(s3[0]) * 1000 + int(s3[1])  
        sec2 = sec1+1-s4
        return sec2, sec1 #sec1+1은 끝난후
    
    lst = []
    for line in lines:
        # h 11:13, m 14:16, s 17:19 & 20:23
        sec1, sec2 = get_time(line)
        lst.append((sec1, sec2))

    # 초기값
    maxV = 1
    for i in range(len(lst)-1):
        origin = lst[i][1]
        now = 1
        for j in range(i+1, len(lst)):
            if origin + 4000 <= lst[j][1]:
                break
            if origin + 1000 > lst[j][0]:
                now += 1
                maxV = max(maxV, now)
    return maxV