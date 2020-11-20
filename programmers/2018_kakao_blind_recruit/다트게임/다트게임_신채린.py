def solution(dartResult):
    number = 0
    score = 0
    letter = ''
    sols = []
    for (index, i) in enumerate(dartResult):
        if i.isdigit() == True:
            number = int(i)
            if number == 0 and dartResult[index-1] == "1":
                number = 10
                
        elif i.isalpha() == True:
            if i == 'S':
                letter = 1
            elif i == 'D':
                letter = 2
            else: 
                letter = 3
            score = number ** letter
            sols.append(score)
        else:
            if i == '*':
                if len(sols) == 1:
                    sols[-1] = sols[-1] * 2
                else:
                    sols[-1] = sols[-1] * 2
                    sols[-2] = sols[-2] * 2
            else:
                sols[-1] = sols[-1] * -1
    total = 0
    for i in sols:
        total += i
    return total

# 테스트 1 〉	통과 (0.03ms, 10.4MB)
# 테스트 2 〉	통과 (0.02ms, 10.3MB)
# 테스트 3 〉	통과 (0.03ms, 10.4MB)
# 테스트 4 〉	통과 (0.02ms, 10.3MB)
# 테스트 5 〉	통과 (0.03ms, 10.3MB)
# 테스트 6 〉	통과 (0.03ms, 10.4MB)
# 테스트 7 〉	통과 (0.02ms, 10.2MB)
# 테스트 8 〉	통과 (0.03ms, 10.4MB)
# 테스트 9 〉	통과 (0.03ms, 10.4MB)
# 테스트 10 〉	통과 (0.03ms, 10.3MB)
# 테스트 11 〉	통과 (0.03ms, 10.4MB)
# 테스트 12 〉	통과 (0.03ms, 10.3MB)
# 테스트 13 〉	통과 (0.03ms, 10.4MB)
# 테스트 14 〉	통과 (0.03ms, 10.4MB)
# 테스트 15 〉	통과 (0.03ms, 10.4MB)
# 테스트 16 〉	통과 (0.03ms, 10.3MB)
# 테스트 17 〉	통과 (0.03ms, 10.4MB)
# 테스트 18 〉	통과 (0.04ms, 10.4MB)
# 테스트 19 〉	통과 (0.03ms, 10.3MB)
# 테스트 20 〉	통과 (0.04ms, 10.4MB)
# 테스트 21 〉	통과 (0.03ms, 10.3MB)
# 테스트 22 〉	통과 (0.03ms, 10.4MB)
# 테스트 23 〉	통과 (0.03ms, 10.4MB)
# 테스트 24 〉	통과 (0.03ms, 10.4MB)
# 테스트 25 〉	통과 (0.03ms, 10.3MB)
# 테스트 26 〉	통과 (0.02ms, 10.4MB)
# 테스트 27 〉	통과 (0.03ms, 10.5MB)
# 테스트 28 〉	통과 (0.03ms, 10.4MB)
# 테스트 29 〉	통과 (0.03ms, 10.4MB)
# 테스트 30 〉	통과 (0.02ms, 10.2MB)
# 테스트 31 〉	통과 (0.03ms, 10.4MB)
# 테스트 32 〉	통과 (0.02ms, 10.4MB)