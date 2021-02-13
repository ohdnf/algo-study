def solution(msg):
    default_dict = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
        'I': 9,
        'J': 10,
        'K': 11,
        'L': 12,
        'M': 13,
        'N': 14,
        'O': 15,
        'P': 16,
        'Q': 17,
        'R': 18,
        'S': 19,
        'T': 20,
        'U': 21,
        'V': 22,
        'W': 23,
        'X': 24,
        'Y': 25,
        'Z': 26  
    }
    
    answer = []
    i = 0
    while i < len(msg):
        cnt = 0
        temp = 0
        while True:
            try:
                if i+cnt < len(msg):
                    temp = default_dict[msg[i:i+cnt+1]]
                    cnt += 1
                else:
                    answer.append(temp)
                    i += cnt
                    break
            except:
                answer.append(temp)
                default_dict[msg[i:i+cnt+1]] = len(default_dict) + 1
                i += cnt
                break

    return answer

'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.50ms, 10.3MB)
테스트 5 〉	통과 (0.04ms, 10.2MB)
테스트 6 〉	통과 (0.79ms, 10.3MB)
테스트 7 〉	통과 (0.48ms, 10.2MB)
테스트 8 〉	통과 (0.59ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.57ms, 10.1MB)
테스트 11 〉	통과 (0.49ms, 10.2MB)
테스트 12 〉	통과 (0.68ms, 10.2MB)
테스트 13 〉	통과 (1.05ms, 10.3MB)
테스트 14 〉	통과 (1.00ms, 10.2MB)
테스트 15 〉	통과 (1.00ms, 10.3MB)
테스트 16 〉	통과 (0.77ms, 10.2MB)
테스트 17 〉	통과 (0.60ms, 10.1MB)
테스트 18 〉	통과 (0.21ms, 10.1MB)
테스트 19 〉	통과 (0.27ms, 10.3MB)
테스트 20 〉	통과 (0.60ms, 10.2MB)
'''