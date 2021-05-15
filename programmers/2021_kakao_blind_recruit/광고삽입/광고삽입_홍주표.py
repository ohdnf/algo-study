def str2sec(hhmmss):
    hh, mm, ss = hhmmss.split(':')
    return int(hh) * 3600 + int(mm) * 60 + int(ss)


def sec2str(ss):
    hh, ss = divmod(ss, 3600)
    mm, ss = divmod(ss, 60)
    return f'{hh:02}:{mm:02}:{ss:02}'


def solution(play_time, adv_time, logs):
    if play_time == adv_time:
        return '00:00:00'

    logs_start = []
    logs_end = []
    play_time = str2sec(play_time)
    adv_time = str2sec(adv_time)
    
    for log in logs:
        h1m1s1, h2m2s2 = log.split('-')
        logs_start.append(str2sec(h1m1s1))
        logs_end.append(str2sec(h2m2s2))

    total_time = [0] * 360000   # 100 * 60 * 60

    for i in range(len(logs)):
        total_time[logs_start[i]] += 1
        total_time[logs_end[i]] -= 1

    for i in range(1, play_time):
        total_time[i] += total_time[i - 1]

    for i in range(1, play_time):
        total_time[i] += total_time[i - 1]

    max_time = total_time[adv_time - 1]
    answer = 0
    for i in range(adv_time, play_time):
        if max_time < total_time[i] - total_time[i - adv_time]:
            max_time = total_time[i] - total_time[i - adv_time]
            answer = i - adv_time + 1
    
    return sec2str(answer)

if __name__ == '__main__':
    print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00",
          "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]), "01:30:59")
    print(solution("99:59:59", "25:00:00", [
          "69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]), "01:00:00")
    print(solution("50:00:00", "50:00:00", [
          "15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]), "00:00:00")


"""
정확성  테스트
테스트 1 〉	통과 (4.26ms, 13MB)
테스트 2 〉	통과 (10.54ms, 13.8MB)
테스트 3 〉	통과 (18.21ms, 14.6MB)
테스트 4 〉	통과 (192.62ms, 31.9MB)
테스트 5 〉	통과 (313.56ms, 41.7MB)
테스트 6 〉	통과 (109.76ms, 21.5MB)
테스트 7 〉	통과 (434.41ms, 56.8MB)
테스트 8 〉	통과 (434.55ms, 61.5MB)
테스트 9 〉	통과 (578.14ms, 79.6MB)
테스트 10 〉	통과 (656.43ms, 80MB)
테스트 11 〉	통과 (632.12ms, 77.3MB)
테스트 12 〉	통과 (622.13ms, 75.2MB)
테스트 13 〉	통과 (616.09ms, 79.9MB)
테스트 14 〉	통과 (505.47ms, 65.2MB)
테스트 15 〉	통과 (44.87ms, 16.8MB)
테스트 16 〉	통과 (493.64ms, 64.4MB)
테스트 17 〉	통과 (612.70ms, 80.1MB)
테스트 18 〉	통과 (553.66ms, 69MB)
테스트 19 〉	통과 (3.82ms, 13MB)
테스트 20 〉	통과 (4.03ms, 13MB)
테스트 21 〉	통과 (140.74ms, 24.6MB)
테스트 22 〉	통과 (0.00ms, 20.2MB)
테스트 23 〉	통과 (550.07ms, 73.4MB)
테스트 24 〉	통과 (534.23ms, 66.7MB)
테스트 25 〉	통과 (81.13ms, 20.2MB)
테스트 26 〉	통과 (55.06ms, 16.3MB)
테스트 27 〉	통과 (64.06ms, 18.5MB)
테스트 28 〉	통과 (62.38ms, 17.8MB)
테스트 29 〉	통과 (59.83ms, 17.9MB)
테스트 30 〉	통과 (39.91ms, 15.8MB)
테스트 31 〉	통과 (46.71ms, 16.1MB)
"""