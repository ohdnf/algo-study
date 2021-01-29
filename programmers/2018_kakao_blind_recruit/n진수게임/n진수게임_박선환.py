def solution(n, t, m, p):
    info = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }
    
    def convert(num, n):
        if not num:
            return '0'
        result = ''
        while num:
            num, remain = divmod(num, n)
            result = info[remain] + result
        return result
        
    answer = ''
    count = 0
    cur_num = 0
    cur_str = ''
    while count < t:
        cur_str += convert(cur_num, n)
        if len(cur_str) >= m*count + p:
            answer += cur_str[m*count + p - 1]
            count += 1
        cur_num += 1
            
    return answer

'''
풀이 시간: 24분

정확성 테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.2MB)
테스트 5 〉	통과 (0.16ms, 10.3MB)
테스트 6 〉	통과 (0.16ms, 10.3MB)
테스트 7 〉	통과 (0.15ms, 10.2MB)
테스트 8 〉	통과 (0.17ms, 10.3MB)
테스트 9 〉	통과 (0.18ms, 10.3MB)
테스트 10 〉	통과 (0.20ms, 10.3MB)
테스트 11 〉	통과 (0.20ms, 10.2MB)
테스트 12 〉	통과 (0.19ms, 10.2MB)
테스트 13 〉	통과 (0.21ms, 10.1MB)
테스트 14 〉	통과 (21.87ms, 10.3MB)
테스트 15 〉	통과 (32.76ms, 10.5MB)
테스트 16 〉	통과 (22.04ms, 10.4MB)
테스트 17 〉	통과 (1.25ms, 10.3MB)
테스트 18 〉	통과 (1.23ms, 10.1MB)
테스트 19 〉	통과 (0.49ms, 10.1MB)
테스트 20 〉	통과 (1.38ms, 10.3MB)
테스트 21 〉	통과 (5.71ms, 10.3MB)
테스트 22 〉	통과 (2.88ms, 10.3MB)
테스트 23 〉	통과 (7.91ms, 10.3MB)
테스트 24 〉	통과 (10.50ms, 10.3MB)
테스트 25 〉	통과 (8.29ms, 10.3MB)
테스트 26 〉	통과 (3.80ms, 10.3MB)
'''