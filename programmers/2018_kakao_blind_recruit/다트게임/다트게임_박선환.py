def solution(dartResult):
    answer = 0
    multiple = ['S', 'D', 'T']
    options = ['*', '#']
    current = 0
    previous = 0
    skip = False
    for i in range(len(dartResult)):
        if skip:
            skip = False
            continue
        c = dartResult[i]
        if c in multiple:
            if c == 'S':
                pass
            elif c == 'D':
                current = current ** 2
            else:
                current = current ** 3
        elif c in options:
            if c == '*':
                current *= 2
                answer += previous
            else:
                current = -current
        else:
            answer += current
            previous = current
            if c == '1' and i+1 < len(dartResult):
                if dartResult[i+1] == '0':
                    current = 10
                    skip = True
                    continue
            current = int(c)
    
    answer += current
    
    return answer

# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.03ms, 10.4MB)
# 테스트 3 〉	통과 (0.03ms, 10.4MB)
# 테스트 4 〉	통과 (0.01ms, 10.3MB)
# 테스트 5 〉	통과 (0.03ms, 10.4MB)
# 테스트 6 〉	통과 (0.03ms, 10.4MB)
# 테스트 7 〉	통과 (0.03ms, 10.4MB)
# 테스트 8 〉	통과 (0.02ms, 10.4MB)
# 테스트 9 〉	통과 (0.03ms, 10.4MB)
# 테스트 10 〉	통과 (0.03ms, 10.4MB)
# 테스트 11 〉	통과 (0.04ms, 10.4MB)
# 테스트 12 〉	통과 (0.03ms, 10.5MB)
# 테스트 13 〉	통과 (0.03ms, 10.4MB)
# 테스트 14 〉	통과 (0.03ms, 10.4MB)
# 테스트 15 〉	통과 (0.03ms, 10.4MB)
# 테스트 16 〉	통과 (0.03ms, 10.4MB)
# 테스트 17 〉	통과 (0.03ms, 10.3MB)
# 테스트 18 〉	통과 (0.03ms, 10.4MB)
# 테스트 19 〉	통과 (0.03ms, 10.5MB)
# 테스트 20 〉	통과 (0.02ms, 10.4MB)
# 테스트 21 〉	통과 (0.03ms, 10.4MB)
# 테스트 22 〉	통과 (0.02ms, 10.3MB)
# 테스트 23 〉	통과 (0.03ms, 10.4MB)
# 테스트 24 〉	통과 (0.03ms, 10.5MB)
# 테스트 25 〉	통과 (0.02ms, 10.4MB)
# 테스트 26 〉	통과 (0.03ms, 10.4MB)
# 테스트 27 〉	통과 (0.02ms, 10.3MB)
# 테스트 28 〉	통과 (0.03ms, 10.5MB)
# 테스트 29 〉	통과 (0.03ms, 10.4MB)
# 테스트 30 〉	통과 (0.03ms, 10.4MB)
# 테스트 31 〉	통과 (0.02ms, 10.3MB)
# 테스트 32 〉	통과 (0.03ms, 10.3MB)