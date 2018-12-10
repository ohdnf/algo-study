def solution(n, t, m, timetable):
    #셔틀 운행 횟수 n, 셔틀 운행 간격 t, 한 셔틀에 탈 수 있는 최대 크루 수 m, 
    #크루가 대기열에 도착하는 시각을 모은 배열 timetable
    answer = ''
    # 시간마다 분단위로 만들어 array에 저장한다.
    timetable = [int(time[:2])*60 + int(time[3:5]) for time in timetable]
    # 시간이 뒤죽박죽이므로 정렬한다.
    timetable.sort()
    # 마지막 버스 운행 시각을 구한다. (첫 출발은 9시 이므로 운행 횟수에서 1을 뺀다)
    last_time = (60*9) + (n-1)*t
    # 운행 횟수만큼 돌면서 
    for i in range(n):
        # 만약 크루의 수보다 탈 수 있는 최대 크루수가 더 크다면 
        if len(timetable) < m: 
            return '%02d:%02d'%(last_time//60,last_time%60)
        # 만약 현재 운행 횟수가 마지막이라면?
        if i == n - 1:
            # timetable의 첫번재 index가 마지막 시간과 같거나 더 이르다면 
            if timetable[0] <= last_time:  
                last_time = timetable[m-1] - 1
            return '%02d:%02d'%(last_time//60,last_time%60)
        # 최대 크루 수를 기준으로 거꾸로 살펴본다면
        for j in range(m-1, -1, -1):
            bus_arrive = (60*9) + i * t
            if timetable[j] <= bus_arrive:
                del timetable[j]