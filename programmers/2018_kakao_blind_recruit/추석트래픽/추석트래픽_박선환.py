def solution(lines):
    import datetime
    answer = 0
    
    # lines => start, end 시간 데이터로 변환
    new_lines = []
    for line in lines:
        end = datetime.datetime.strptime(line[11:23], '%H:%M:%S.%f')
        time = datetime.timedelta(seconds=float(line[24:-1]), microseconds=-1000)
        start = end - time
        new_lines.append((start, end))
        
    # 각 lines의 start, end 각각 point마다의 1초 구간에서 겹치는 line 수 세기
    for line in new_lines:
        for point in line:
            p_start = point
            p_end = p_start + datetime.timedelta(seconds=1, microseconds=-1000)
            count = 0
            for (start, end) in new_lines:
                if start > p_end or end < p_start:
                    continue
                count += 1
            if count > answer:
                answer = count
        
    return answer

'''
테스트 1 〉	통과 (2.15ms, 10.8MB)
테스트 2 〉	통과 (89.13ms, 11MB)
테스트 3 〉	통과 (115.52ms, 11MB)
테스트 4 〉	통과 (2.66ms, 10.8MB)
테스트 5 〉	통과 (5.16ms, 10.8MB)
테스트 6 〉	통과 (5.23ms, 10.8MB)
테스트 7 〉	통과 (94.52ms, 11.1MB)
테스트 8 〉	통과 (91.80ms, 11MB)
테스트 9 〉	통과 (4.28ms, 10.8MB)
테스트 10 〉	통과 (2.83ms, 10.7MB)
테스트 11 〉	통과 (2.90ms, 10.8MB)
테스트 12 〉	통과 (95.03ms, 11.1MB)
테스트 13 〉	통과 (5.16ms, 10.8MB)
테스트 14 〉	통과 (2.75ms, 10.7MB)
테스트 15 〉	통과 (2.53ms, 10.9MB)
테스트 16 〉	통과 (2.63ms, 10.9MB)
테스트 17 〉	통과 (2.40ms, 10.8MB)
테스트 18 〉	통과 (545.86ms, 11.3MB)
테스트 19 〉	통과 (335.20ms, 11.3MB)
테스트 20 〉	통과 (361.06ms, 11.3MB)
테스트 21 〉	통과 (2.31ms, 10.8MB)
테스트 22 〉	통과 (2.58ms, 10.8MB)
'''