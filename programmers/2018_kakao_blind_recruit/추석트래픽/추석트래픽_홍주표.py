def solution(lines):
    """
    소수점 셋째 자리 = 0.001초 단위
    """
    logs = []
    for line in lines:
        _, hmsms, proc = line.split()
        h, m, sms = hmsms.split(':')
        s, ms = sms.split('.')
        finish = 86400000 + int(h) * 60 * 60 * 1000 + int(m) * 60 * 1000 + int(s) * 1000 + int(ms)
        proc = int(float(proc[:-1]) * 1000)
        logs.append([finish-proc+1, finish])
    
    max_traffic = 0
    for i in range(len(logs)):
        front_traffic = 0
        front = logs[i][0] - 999
        for j in range(len(logs)):
            if logs[j][1] - 3000 >= logs[i][0]:
                break
            if logs[j][1] < front or logs[i][0] < logs[j][0]:
                continue
            else:
                front_traffic += 1
                
        back_traffic = 0
        back = logs[i][1] + 999
        for j in range(len(logs)):
            if logs[j][1] - 3000 >= back:
                break
            if back < logs[j][0] or logs[j][1] < logs[i][1]:
                continue
            else:
                back_traffic += 1
        
        max_traffic = max(max_traffic, front_traffic, back_traffic)
            
    
    return max_traffic

"""
테스트 1 〉	통과 (0.14ms, 10.5MB)
테스트 2 〉	통과 (178.98ms, 10.4MB)
테스트 3 〉	통과 (289.56ms, 10.5MB)
테스트 4 〉	통과 (0.04ms, 10.5MB)
테스트 5 〉	통과 (5.03ms, 10.4MB)
테스트 6 〉	통과 (4.74ms, 10.4MB)
테스트 7 〉	통과 (175.92ms, 10.4MB)
테스트 8 〉	통과 (176.88ms, 10.5MB)
테스트 9 〉	통과 (2.59ms, 10.5MB)
테스트 10 〉	통과 (0.11ms, 10.5MB)
테스트 11 〉	통과 (0.14ms, 10.4MB)
테스트 12 〉	통과 (175.08ms, 10.5MB)
테스트 13 〉	통과 (5.41ms, 10.4MB)
테스트 14 〉	통과 (0.04ms, 10.5MB)
테스트 15 〉	통과 (0.04ms, 10.4MB)
테스트 16 〉	통과 (0.04ms, 10.4MB)
테스트 17 〉	통과 (0.04ms, 10.5MB)
테스트 18 〉	통과 (1681.64ms, 10.7MB)
테스트 19 〉	통과 (700.23ms, 10.6MB)
테스트 20 〉	통과 (701.39ms, 10.7MB)
테스트 21 〉	통과 (0.04ms, 10.4MB)
테스트 22 〉	통과 (0.03ms, 10.5MB)
"""
