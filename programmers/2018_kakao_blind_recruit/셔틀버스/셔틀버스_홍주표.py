def solution(n, t, m, timetable):
    """
    셔틀버스는 09:00부터 n회 t분 간격으로 운행
    버스 1대에 최대 m명 탑승 가능
    timetable은 다른 크루들 정거장 도착시간
    """

    # 버스 시간표 만들기
    last = 540 + (n - 1) * t
    departures = []
    for stop_time in range(540, last + 1, t):
        departures.append(f'{stop_time // 60:02d}:{stop_time % 60:02d}')
    # print(departures)

    timetable.sort()

    # 막차 직전까지 처리
    last = departures[-1]

    while departures[0] != last:
        depart_time = departures.pop(0)
        on_board = 0
        while timetable and on_board < m:
            if timetable[0] <= depart_time:
                timetable.pop(0)
                on_board += 1
            else:
                break

    # print(timetable)
    # print(departures, last)

    # 콘은 막차의 맨 마지막 탑승객이 되어야 한다.
    times = set()
    last_on_board = 0
    while timetable and last_on_board < m:
        if timetable[0] <= last:
            times.add(timetable.pop(0))
            last_on_board += 1
        else:
            break

    print('----------------')
    print(timetable)
    print(last_on_board, m)

    # 만원일 경우
    if last_on_board == m:
        times = list(times)
        times.sort()
        print(times)
        h, m = times[-1].split(':')
        safe_time = int(h) * 60 + int(m) - 1
        answer = f'{safe_time // 60:02d}:{safe_time % 60:02d}'
    # 자리가 남을 경우
    else:
        answer = last

    return answer


if __name__ == '__main__':
    print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]), "09:00")
    print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]), "09:09")
    print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]), "08:59")
    print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]), "00:00")
    print(solution(1, 1, 1, ["23:59"]), "09:00")
    print(solution(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
                                "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]),
          "18:00")
    print(solution(10, 60, 10, ["17:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
                                "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]), "18:00")


"""
정확성 테스트
테스트 1 〉	통과 (0.02ms, 10.4MB)
테스트 2 〉	통과 (0.04ms, 10.5MB)
테스트 3 〉	통과 (0.04ms, 10.5MB)
테스트 4 〉	통과 (0.03ms, 10.4MB)
테스트 5 〉	통과 (0.06ms, 10.5MB)
테스트 6 〉	통과 (0.04ms, 10.5MB)
테스트 7 〉	통과 (0.19ms, 10.6MB)
테스트 8 〉	통과 (0.04ms, 10.6MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.04ms, 10.6MB)
테스트 11 〉	통과 (0.03ms, 10.4MB)
테스트 12 〉	통과 (0.18ms, 10.5MB)
테스트 13 〉	통과 (0.17ms, 10.4MB)
테스트 14 〉	통과 (0.06ms, 10.5MB)
테스트 15 〉	통과 (0.08ms, 10.5MB)
테스트 16 〉	통과 (0.11ms, 10.6MB)
테스트 17 〉	통과 (0.19ms, 10.5MB)
테스트 18 〉	통과 (0.10ms, 10.4MB)
테스트 19 〉	통과 (0.14ms, 10.5MB)
테스트 20 〉	통과 (0.14ms, 10.6MB)
테스트 21 〉	통과 (0.13ms, 10.5MB)
테스트 22 〉	통과 (0.67ms, 10.5MB)
테스트 23 〉	통과 (0.51ms, 10.6MB)
테스트 24 〉	통과 (0.24ms, 10.5MB)
"""