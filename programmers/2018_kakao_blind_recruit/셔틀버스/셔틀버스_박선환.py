# 첫 번째 시도
def solution(n, t, m, timetable):
    import datetime
    answer = ''

    last_time = datetime.datetime.strptime('09:00', '%H:%M') + datetime.timedelta(minutes=(n-1)* t)
    last_time = last_time.strftime('%H:%M')

    timetable.sort()
    i = 0
    j = 0
    bus_time = '09:00'
    if len(timetable) < n*m:
        max_num = len(timetable)
    else:
        max_num = n*m

    while i < max_num:
        if timetable[i] > last_time:
            answer = last_time
            break
        if timetable[i] <= bus_time:
            j += 1
            if j == m:
                j = 0
                n -= 1
                if not n:
                    break
            i += 1
        else:
            bus_time = datetime.datetime.strptime(bus_time, '%H:%M') + datetime.timedelta(minutes=t)
            bus_time = bus_time.strftime('%H:%M')
            j = 0
            n -= 1
            if not n:
                break

    if not answer:
        if j == 0:
            answer = datetime.datetime.strptime(timetable[i], '%H:%M') - datetime.timedelta(minutes=1)
            answer = answer.strftime('%H:%M')
        else:
            answer = bus_time

        if n and answer < last_time:
            answer = last_time

    return answer

'''
테스트 1 〉	통과 (2.34ms, 10.9MB)
테스트 2 〉	통과 (2.55ms, 10.9MB)
테스트 3 〉	통과 (2.22ms, 10.8MB)
테스트 4 〉	통과 (4.18ms, 10.8MB)
테스트 5 〉	실패 (2.37ms, 10.8MB)
테스트 6 〉	통과 (2.36ms, 10.9MB)
테스트 7 〉	통과 (9.94ms, 10.9MB)
테스트 8 〉	통과 (4.82ms, 10.9MB)
테스트 9 〉	통과 (2.45ms, 10.9MB)
테스트 10 〉	통과 (2.39ms, 10.8MB)
테스트 11 〉	통과 (3.85ms, 10.8MB)
테스트 12 〉	통과 (4.86ms, 10.8MB)
테스트 13 〉	통과 (2.63ms, 10.8MB)
테스트 14 〉	통과 (2.45ms, 10.9MB)
테스트 15 〉	통과 (2.39ms, 10.8MB)
테스트 16 〉	통과 (33.93ms, 10.9MB)
테스트 17 〉	통과 (2.42ms, 10.9MB)
테스트 18 〉	통과 (4.81ms, 10.9MB)
테스트 19 〉	통과 (2.43ms, 10.8MB)
테스트 20 〉	통과 (2.65ms, 10.9MB)
테스트 21 〉	통과 (2.36ms, 10.9MB)
테스트 22 〉	통과 (2.88ms, 10.9MB)
테스트 23 〉	통과 (2.83ms, 11MB)
테스트 24 〉	실패 (4.98ms, 10.9MB)
'''