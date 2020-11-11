def solution(dartResult):
    result = []
    before = ''
    for string in dartResult:
        if string in ('S', 'D', 'T', '*', '#'):
            result.append(before)
            result.append(string)
            before = ''
        else:
            before += string

    score = []

    for s in result:
        if s.isdigit():
            score.append(int(s))
        elif s == '*':
            curr_point = score.pop()
            curr_point *= 2
            if score:
                score[-1] *= 2
            score.append(curr_point)
        elif s == '#':
            score[-1] *= -1
        elif s == 'D':
            score[-1] **= 2
        elif s == 'T':
            score[-1] **= 3
        else:
            continue

    return sum(score)


"""
정확성 테스트
테스트 1 〉	통과 (0.02ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (0.03ms, 10.5MB)
테스트 5 〉	통과 (0.03ms, 10.4MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
테스트 7 〉	통과 (0.03ms, 10.4MB)
테스트 8 〉	통과 (0.02ms, 10.4MB)
테스트 9 〉	통과 (0.03ms, 10.3MB)
테스트 10 〉	통과 (0.03ms, 10.3MB)
테스트 11 〉	통과 (0.03ms, 10.3MB)
테스트 12 〉	통과 (0.04ms, 10.4MB)
테스트 13 〉	통과 (0.04ms, 10.5MB)
테스트 14 〉	통과 (0.04ms, 10.4MB)
테스트 15 〉	통과 (0.03ms, 10.3MB)
테스트 16 〉	통과 (0.03ms, 10.4MB)
테스트 17 〉	통과 (0.93ms, 10.4MB)
테스트 18 〉	통과 (0.04ms, 10.5MB)
테스트 19 〉	통과 (0.03ms, 10.4MB)
테스트 20 〉	통과 (0.03ms, 10.4MB)
테스트 21 〉	통과 (0.04ms, 10.3MB)
테스트 22 〉	통과 (0.04ms, 10.4MB)
테스트 23 〉	통과 (0.03ms, 10.4MB)
테스트 24 〉	통과 (0.04ms, 10.4MB)
테스트 25 〉	통과 (0.03ms, 10.4MB)
테스트 26 〉	통과 (0.04ms, 10.2MB)
테스트 27 〉	통과 (0.04ms, 10.4MB)
테스트 28 〉	통과 (0.03ms, 10.3MB)
테스트 29 〉	통과 (0.04ms, 10.4MB)
테스트 30 〉	통과 (0.03ms, 10.6MB)
테스트 31 〉	통과 (0.04ms, 10.3MB)
테스트 32 〉	통과 (0.04ms, 10.5MB)
"""